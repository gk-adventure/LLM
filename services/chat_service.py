from openai import OpenAI
import os
from datetime import datetime
import json

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# 구조화된 json 형식
tools = [{
    "type": "function",
    "function": {
        "name": "save_expense",
        "description": "사용자의 소비 내역을 파싱하여 금액과 카테고리, 날짜, 메모를 저장",
        "parameters": {
            "type": "object",
            "properties": {
                "save_type": {
                    "type": "integer",
                    "description": "소비 내역이 수입이면 0, 지출이면 1 반환"
                },
                "category": {
                    "type": "string",
                    "enum": ["카페", "식비", "교통", "의류", "문화", "공과금", "기타", "월급", "용돈"],
                    "description": "정해진 카테고리 중 하나 수입이면 '월급', '용돈', '기타'에서 선택, 지출이면 '카페', '식비', '교통', '의류', '문화', '공과금', '기타'에서 선택"
                },
                "amount": {
                    "type": "integer",
                    "description": "금액 (숫자만, 원단위)"
                },
                "date": {
                    "type": "string",
                    "description": "소비 날짜 (YYYY-MM-DD 형식)"
                },
                "description": {
                    "type": "string",
                    "description": "소비에 대한 메모"
                }
            },
            "required": ["save_type", "category", "amount", "date"],
            "additionalProperties": False
        }
    },
    "strict": True
}]

# 입력 메시지가 소비내역 저장인지 피드백 반환인지 구분
def handle_message(message: str):

    # 현재 날짜를 YYYY-MM-DD 형식으로 저장 (날짜 저장을 위해 사용)
    today = datetime.today().strftime("%Y-%m-%d")

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": f"""
             너는 사용자 소비 내역을 정리해주는 가계부 어시스턴트야.
             오늘 날짜는 {today}야.
             만약 소비자가 '오늘', '어제', '그제'와 같은 말들을 하면 이를 기준으로 정확한 날짜(YYYY-MM-DD 형식)로 변환해서 바꿔줘.
             소비 내역을 말하면 수입인지 지출인지 판단하여 반환하고, 카테고리와 금액, 날짜, 메모를 파싱해서 JSON 형태로 반환해줘.
             소비 내역을 저장하는 입력이 아닌 소비 방식과 같은 질문에는 그에 대한 피드백을 반환해줘. 또한 일반적인 질문이나 조언(피드백) 요청이면 텍스트로 답변해줘."""},
             {"role": "user", "content": message}
        ],
        tools=tools,
        tool_choice="auto"
    )

    msg = response.choices[0].message

    # 도구 호출이 있는 경우 (소비 내역 저장 요청일 경우)
    if msg.tool_calls:
        args = json.loads(msg.tool_calls[0].function.arguments)
        return {
            "type": "save_expense",
            "reply": f"{args['category']} 카테고리로 {args['amount']}원을 기록했어요.",
            "data": {
                "save_type": args["save_type"],
                "category": args["category"], 
                "amount": args["amount"],
                "date": args["date"],
                "description": args["description"]
            }
        }
    else:
        # 도구 호출이 없는 경우 (피드백 요청일 경우)
        return {
            "type": "feedback",
            "reply": msg.content
        }