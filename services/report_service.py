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
        "소비 요약": {{
            "총 소비 금액": 76600,
            "예산 대비 소비 비율": 25.5
            "주요 소비 카테고리": ["식비", "커피"],
            "카테고리별 지출 금액": {{
                "식비": 69000,
                "커피": 7600
            }}
        }},
        "소비 패턴 분석": "일회성 날짜(6월 2일)에 모든 기록이 집중되어 있어 특정 날에 지출이 집중된 것으로 보입니다. 술 약속과 스타벅스 커피 지출이 비교적 크며, 술 약속이 가장 큰 지출 항목입니다. 하루 식비 총액(6월 2일 기준)은 6,000 + 14,000 + 15,000 + 34,000 = 69,000원으로 다소 높은 편입니다. 전체 예산 대비 이번 달 소비는 적은 편이나, 특정 일에 집중된 소비가 관찰됩니다."
        
        "피드백 및 제안": 
            "특정 날짜에 소비가 몰리는 경향이 있어, 일정 기간 동안 소비를 분산시키는 것이 예산 관리에 도움이 될 수 있습니다. 술 약속 지출이 상당하므로 기회가 된다면 횟수나 금액을 조절하여 건강과 경제적 부담을 줄일 수 있습니다. 커피 등 소소한 지출도 누적되면 부담이 되므로, 커피 소비 빈도나 가성비 좋은 대안을 고려해보세요. 월간 예산 300,000원 대비 이번 달 실제 소비가 25% 수준으로 적절히 관리되고 있으니 현재 소비 습관에서 조금만 더 신경 쓰면 좋은 재정 상태를 유지할 수 있습니다."
    }}

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
