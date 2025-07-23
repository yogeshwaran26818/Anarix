import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Load API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in environment variables.")

# Configure Gemini with correct model name and key
genai.configure(api_key=api_key)

# Use correct model name (not 'models/gemini-pro')
model = genai.GenerativeModel("models/gemini-2.5-pro")  


def question_to_sql(question: str) -> str:
    prompt = f"""
You are a helpful data analyst assistant.

Convert the following user question into a valid SQLite SQL query.

Rules:
- DO NOT wrap SQL in ```sql ... ```
- DO NOT use single quotes (' ') or square brackets [ ] for column names.
- IF a column has spaces (e.g., Total Ordered Product Sales), wrap it in double quotes: "Total Ordered Product Sales"
- Use table names and column names exactly as provided below.

Available Tables:
- total_sales: Columns = [item_id, date, total_sales, total_units_ordered]
- ad_sales: Columns = [asin, item_id, date, impressions, clicks, ad_sales, ad_spend]
- eligibility: Columns = [asin, item_id, eligible]

Important Notes:
- CPC (Cost Per Click) per product = SUM(ad_spend) / SUM(clicks) GROUPED BY item_id
  To find the highest CPC, return the item_id with the MAX CPC from the grouped result
- For RoAS (Return on Ad Spend), calculate it as: 
  (SELECT SUM(ad_sales) FROM ad_sales WHERE ad_spend != 0) / 
  (SELECT SUM(ad_spend) FROM ad_sales WHERE ad_spend != 0)
- Only include records where denominator ≠ 0 to avoid division errors.

Question: {question}
SQL:
"""


    try:
        response = model.generate_content(prompt)
        sql = response.text.strip()

        # ✅ Remove any accidental code blocks (extra safety)
        if sql.startswith("```"):
            sql = sql.replace("```sql", "").replace("```", "").strip()
        return sql
    except Exception as e:
        return f"❌ [Gemini API Error] {str(e)}"



