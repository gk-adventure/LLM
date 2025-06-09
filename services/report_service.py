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
    사용자 {request.userId}의 {request.month} 월 소비 내역이야. 사용자의 해당 월 예산은 {request.monthBudget}원이야.
    아래 데이터를 바탕으로 월간 소비 습관을 요약하고 분석해줘. 그리고 피드백도 함께 제공해줘.

    반환 형식은 아래 예시처럼 반환해줘.
    {{
    "totalSpending": number,                       // 총 소비 금액 (숫자)
    "budgetUsageRate": number,                    // 예산 대비 소비율 (퍼센트 숫자)
    "topCategories": [string],                    // 소비가 높은 카테고리 목록
    "spendingByCategory": {{                       // 카테고리별 소비 금액
        "카테고리명": number
    }},
    "patternAnalysis": string,                    // 소비 패턴 요약 설명
    "feedback": string                            // 사용자 맞춤 피드백
    }}
    반드시 JSON 형식을 지켜서 반환해줘.

    아래는 사용자의 소비 데이터야:
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
    # return response.choices[0].message.content
