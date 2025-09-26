import os
import sys
import pandas as pd
from datetime import datetime
import json

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from schema_description_agent.agent import SchemaDescriptionAgent
from schema_description_agent.config import SchemaDescriptionConfig

def print_header(title):
    print("\n" + "="*80)
    print(f" {title} ".center(80, '='))
    print("="*80)

def main():
    print_header("SCHEMA DESCRIPTION AGENT - BASIC USAGE")
    
    # 1. Create a sample DataFrame
    print("\n🔄 Creating sample data...")
    data = {
        'order_id': [1001, 1002, 1003, 1004, 1005],
        'customer_name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown', 'David Wilson', 'Eva Davis'],
        'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
        'quantity': [1, 2, 1, 1, 2],
        'price': [999.99, 29.99, 59.99, 199.99, 79.99],
        'order_date': pd.to_datetime(['2023-01-15', '2023-01-16', '2023-01-16', '2023-01-17', '2023-01-18']),
        'is_delivered': [True, True, False, True, False]
    }
    df = pd.DataFrame(data)
    
    print("\n📋 Sample Data:")
    print(df.head())
    
    # 2. Initialize the agent
    print("\n🚀 Initializing SchemaDescriptionAgent...")
    config = SchemaDescriptionConfig(
        model_name="gpt-4.1-mini",
        temperature=0.3,
        max_tokens=2000,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    try:
        agent = SchemaDescriptionAgent(config=config)
        print("✅ Agent initialized successfully!")
        
        # 3. Analyze the DataFrame
        print("\n🔍 Analyzing DataFrame structure...")
        analysis = agent._analyze_dataframe(df)
        
        print("\n📊 Analysis Results:")
        print(f"• Rows: {analysis['row_count']}")
        print(f"• Columns: {analysis['column_count']}")
        print(f"• Total cells: {analysis['total_cells']}")
        print(f"• Duplicate rows: {analysis['duplicate_row_count']}")
        print(f"• Missing values: {analysis['missing_cells_total']}")
        
        print("\n📋 Column Details:")
        for col in analysis['column_details']:
            print(f"\n {col['name']} ({col['data_type']})")
            print(f"   Null percentage: {col['null_percentage']}")
            print(f"   Unique percentage: {col['unique_percentage']}")
        
        # 4. Generate table description using the actual LLM
        print("\n🤖 Generating table description using LLM...")
        
        # Make the actual LLM call through the agent
        table_description = agent.generate_table_description(df)
        
        # Log the raw response for debugging
        print("\n🔍 Raw LLM Response:")
        print(json.dumps(table_description.model_dump(), indent=2))
        
        # 5. Display the generated description
        print("\n📜 Generated Table Description:")
        print(f"\nTable: {table_description.tables[0].table_name}")
        print(f"Description: {table_description.tables[0].description}")
        
        print("\nColumn Descriptions:")
        for col in table_description.tables[0].columns:
            print(f"• {col.name}: {col.description}")
        
        print("\n✅  ✅  ✅  ✅  ✅  Basic usage demonstration completed!")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
