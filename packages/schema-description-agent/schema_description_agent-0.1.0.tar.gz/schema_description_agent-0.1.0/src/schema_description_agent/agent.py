import logging
import json
import pandas as pd
from typing import Dict, Any, List, Optional
from datetime import datetime

# Assuming a shared blueprint/framework for core components
from types import SimpleNamespace
from sfn_blueprint import SFNAIHandler, MODEL_CONFIG
from sfn_blueprint import SFNDataLoader
from .constants import format_table_description_prompt
from .config import SchemaDescriptionConfig
from .models import SchemaDescription


class SchemaDescriptionAgent:
    def __init__(self , config: Optional[SchemaDescriptionConfig] = None):
        self.logger = logging.getLogger(__name__)
        self.ai_handler = SFNAIHandler()
        self.data_loader = SFNDataLoader()
        self.config = config or SchemaDescriptionConfig()

    def _analyze_dataframe(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Perform a preliminary statistical analysis of a DataFrame.

        Args:
            df: The pandas DataFrame to analyze.
            table_name: The name of the table.

        Returns:
            A dictionary containing the statistical summary.
        """
        analysis = {
            "row_count": int(df.shape[0]),
            "column_count": int(df.shape[1]),
            "total_cells": int(df.size),
            "duplicate_row_count": int(df.duplicated().sum()),
            "missing_cells_total": int(df.isnull().sum().sum()),
            "column_details": []
        }

        for col in df.columns:
            column_series = df[col]
            unique_count = column_series.nunique()
            null_count = int(column_series.isnull().sum())
            
            col_details = {
                "name": col,
                "data_type": str(column_series.dtype),
                "null_count": null_count,
                "null_percentage": (null_count / analysis["row_count"]) * 100 if analysis["row_count"] > 0 else 0,
                "unique_count": int(unique_count),
                "unique_percentage": (unique_count / analysis["row_count"]) * 100 if analysis["row_count"] > 0 else 0
            }

            # Add specific stats for numeric vs. categorical columns
            if pd.api.types.is_numeric_dtype(column_series):
                stats = column_series.describe().to_dict()
                col_details["stats"] = {k: round(v, 2) for k, v in stats.items()}
            else:
                # Top 5 most frequent values
                value_counts = column_series.value_counts().nlargest(5)
                col_details["top_values"] = {str(k): int(v) for k, v in value_counts.items()}

            analysis["column_details"].append(col_details)
        
        return analysis
    
    def generate_table_description(self, df: pd.DataFrame) -> SchemaDescription:

        statistical_analysis = self._analyze_dataframe(df)
        system_prompt, user_prompt = format_table_description_prompt(json.dumps(statistical_analysis, indent=2))

        print('self.config',self.config)
        response, cost_summary = self.ai_handler.route_to(
            llm_provider=self.config.ai_provider,
            configuration={
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "max_tokens": self.config.max_tokens,
                "temperature": self.config.temperature,
            },
            model=self.config.model_name 
        )
        self.logger.info(f"LLM assessment received. Cost: {cost_summary}")

        try:
            clean_response = response.strip()
            if clean_response.startswith('```json'):
                clean_response = clean_response[7:]  # Remove ```json
            if clean_response.endswith('```'):
                clean_response = clean_response[:-3]
            
            llm_result = json.loads(clean_response)
            return SchemaDescription.model_validate(llm_result)

        except Exception as e:
            self.logger.error(f"An unexpected error occurred during LLM result processing: {e}")
            raise

    def execute_task(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        self.logger.info("Executing data quality assessment task.")
        file = task_data.get('file') 
        if not file:
            return {
                "success": False,
                "error": "No valid 'file' provided in task data.",
                "agent": self.__class__.__name__
            }
        
        df = self.data_loader.execute_task(SimpleNamespace(path=file)) 
        
        if df is None or df.empty:
            return {
                "success": False,
                "error": "Failed to load DataFrame from file.",
                "agent": self.__class__.__name__
            }

        result = self.generate_table_description(df)

        try:
            # Check if we have workflow storage information
            if 'workflow_storage_path' in task_data or 'workflow_id' in task_data:
                from sfn_blueprint import WorkflowStorageManager
                
                # Determine workflow storage path
                workflow_storage_path = task_data.get('workflow_storage_path', 'outputs/workflows')
                workflow_id = task_data.get('workflow_id', 'unknown')
                
                # Initialize storage manager
                storage_manager = WorkflowStorageManager(workflow_storage_path, workflow_id)
                storage_manager.save_agent_result(
                    agent_name=self.__class__.__name__,
                    step_name="table description",
                    data={"quality_reports": result.model_dump()},
                    metadata={"file": file, "execution_time": datetime.now().isoformat()}
                )
                self.logger.info("Table description reports saved to workflow storage.")
        except Exception as e:
            self.logger.warning(f"Failed to save results to workflow storage: {e}")
        
        return {
                "success": True,
                "result": {
                    "table description": result.dict()
                },
                "agent": self.__class__.__name__
            }


