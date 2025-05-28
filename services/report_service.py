from schemas.report_schema import ReportRequest
import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# 월간 리포트 분석 및 생성
def analyze_consumption(request: ReportRequest):

    prompt = f"""
    사용자 {request.userId}의 {request.month} 월 소비 내역이야.
    이 데이터들을 바탕으로 월간 소비 습관을 요약하고 분석하며, 피드백을 제공해줘.
    JSON 형식으로, summary, suggestions, riskCategory(과소비한 카테고리 등)를 포함해줘.
    """

    # json.dumps: python dictionary 타입의 객체를 string타입의 json 형태로 가져옴
    user_data = json.dumps([d.dict() for d in request.data], ensure_ascii=False)
    full_prompt = prompt + "\n" + user_data

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "너는 사용자 소비 내역을 분석하고 피드백을 제공하는 가계부 어시스턴트야."},
            {"role": "user", "content": full_prompt}
        ],
    )

    # json.loads: string 타입의 json 형태를 python dictionary 타입으로 가져옴 
    return json.loads(response.choices[0].message.content)
