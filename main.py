from llm_interface import question_to_sql
from query_executor import execute_query

def ask_question(question: str):
    # Step 1: Convert question to SQL
    sql = question_to_sql(question)
    print(f"[LLM SQL]: {sql}")

    # Step 2: Execute SQL
    result = execute_query(sql)

    # Step 3: Format and return response
    return format_response(result)


def format_response(result):
    if isinstance(result, str):  
        return result
    if not result:
        return "No data found."

    response = ""
    for row in result:
        response += "\n" + ", ".join(f"{k}: {v}" for k, v in row.items())
    return response.strip()

