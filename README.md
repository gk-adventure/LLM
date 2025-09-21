# 🪙 돈굴 돈굴 돈굴이  
**LLM 기반 AI 스마트 가계부 서비스**  
2030 세대의 **지출 절제와 금융 관리**를 돕는 AI 가계부  

<p align="center">
  <img width="1776" height="831" alt="Image" src="https://github.com/user-attachments/assets/b5498774-cfcc-4953-9aa4-3dfdfe9e6dc2" />
</p>



##  프로젝트 개요  
불안한 경제 상황 속에서 **젊은 세대가 소비를 더 스마트하게 관리**할 수 있도록,  
지출 내역을 AI가 자동 분석하고 리포트를 제공하는 가계부 서비스를 개발했습니다.  

- **개발 기간**: 2025.06 (약 2주)  
- **팀 구성**: FE 3명, BE 2명  

해당 깃허브 레포지토리는 FastAPI기반으로 구축된 LLM API 서버입니다.
- 실시간 채팅
- 리포트 생성
  
등의 기능을 API 형태로 제공하며, Docker 지원으로 어디서든 손쉽게 배포 및 실행할 수 있습니다. (현재는 API 키 사용 중단으로 중단된 서비스입니다.)

##  기술 스택  
| 분야       | 기술 |
|------------|----------------------------------|
| Language   | Java, Python |
| Framework  | Spring Boot, FastAPI |
| AI/LLM     | OpenAI GPT-4.1-mini |
| Infra      | AWS EC2, Docker |
| Database   | MySQL |
| Tools      | GitHub, Slack, Trello |

## 아키텍처

<img width="528" height="327" alt="Image" src="https://github.com/user-attachments/assets/06d79f2c-8cb1-47da-9da6-65cfcdecf05f" />


##  주요 기능
**실시간 채팅 API**

사용자 입력을 받아 LLM을 통해 즉시 응답 반환

- 자연어 지출 입력 → JSON 구조화
- 
  `“6월 5일 스타벅스 5300원” → {"date": "2024-06-05", "category": "식비", "amount": 5300, "memo": "스타벅스"}`
  
<br>

**리포트 생성 API**

- AI 소비 분석 리포트
  - 총 소비 / 카테고리별 지출 비율  
  - 예산 대비 소비율  
  - 주차별 소비 패턴 분석  
  - 개선 피드백 자동 제공  


##  서비스 화면
<p align="center">
  <img width="445" height="311" alt="Image" src="https://github.com/user-attachments/assets/425d27ee-5068-4a74-9d48-a4a6038f0bd6" />
  <img width="507" height="308" alt="Image" src="https://github.com/user-attachments/assets/68b90ed4-0671-46f6-a5c5-48fb129b1ee5" />
</p>


##  배포 및 성능 개선
- **멀티 스테이지 Docker 빌드** 적용 → 이미지 크기 `1.44GB → 733MB (약 49% 감소)`  
- **Spring Boot CORS 문제 해결** → `WebMvcConfigurer` 설정으로 프론트와 정상 통신  
- AWS EC2 환경에서 안정적으로 서비스 배포  


## 프로젝트 구조

```bash
ProjectLab_LLM/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── requirements.txt
├── main.py              # FastAPI 앱 실행 및 라우터 설정
├── routers/             # API 엔드포인트 정의
│   ├── chat.py          # 챗봇 대화 (소비내역 저장 / 피드백 요청)
│   └── report.py        # 월별 리포트 생성
├── schemas/             # Pydantic 스키마 정의
│   ├── chat_schema.py
│   └── report_schema.py
└── services/            # 비즈니스 로직
    ├── chat_service.py
    └── report_service.py
```

<br>

## 🔗 API 사용법

### 💬 챗봇 API (소비내역 저장 & 피드백)

* **Endpoint**: `POST /api/chat/`
* **Request Body 예시**:

```json
{
  "userId": 1,
  "message": "오늘 스타벅스에서 아메리카노 4500원 마셨어"
}
```

* **Response 예시 (지출 저장)**:

```json
{
  "type": "save_expense",
  "reply": "카페 카테고리로 4500원을 기록했어요.",
  "data": {
    "userId": 1,
    "saveType": 0,  // 0=지출, 1=수입
    "category": "카페",
    "amount": 4500,
    "date": "2025-06-11",
    "description": "스타벅스 아메리카노"
  }
}
```

* **Response 예시 (피드백)**:

```json
{
  "type": "feedback",
  "reply": "월급이 30만원인데 오늘 15만원을 쓰셨군요. 남은 기간 동안 필수 지출에 집중하시고, 불필요한 소비를 줄이는 게 좋겠습니다.",
  "data": null
}
```

---

### 📊 리포트 API (월별 리포트)

* **Endpoint**: `POST /api/report/`
* **Request Body 예시**:

```json
{
  "userId": 123,
  "month": "2025-05",
  "monthBudget": 500000,
  "data": [
    { "category": "카페", "amount": 12000, "date": "2025-05-01", "description": "커피" },
    { "category": "식비", "amount": 50000, "date": "2025-05-03", "description": "고기" },
    { "category": "의류", "amount": 250000, "date": "2025-05-06", "description": "옷쇼핑" }
  ]
}
```

* **Response 예시 (최종)**:

```json
{
  "userId": 123,
  "month": "2025-05",
  "summary": {
    "totalSpent": 412000,
    "categoryBreakdown": {
      "식비": 150000,
      "카페": 12000,
      "의류": 250000
    },
    "monthlyBudget": 500000,
    "notes": "5월 한 달간 주로 식비와 의류에 많은 지출이 있었으며, 특히 6일 의류 소비가 전체 예산의 절반을 차지했습니다. 카페 지출은 적은 편이지만 식비는 매일 일정하게 누적되어 예산에서 큰 비중을 차지했습니다."
  },
  "suggestions": {
    "식비": "외식 줄이기, 장보기 계획 세우기",
    "의류": "큰 지출 전 계획 수립 권장",
    "전체": "월 지출 점검과 사전 계획으로 예산 관리"
  },
  "riskCategory": ["의류", "식비"]
}
```

## 서비스 데이터 플로우
<img src="https://github.com/user-attachments/assets/aae67854-f9de-4bcf-9343-2195ace8f070" alt="Image" width="50%"/>


## 🔗 링크
- [GitHub - Backend](https://github.com/gk-adventure/Backend)  
- [GitHub - LLM](https://github.com/gk-adventure/LLM)  
