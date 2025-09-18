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


##  기술 스택  
| 분야       | 기술 |
|------------|----------------------------------|
| Language   | Java, Python |
| Framework  | Spring Boot, FastAPI |
| AI/LLM     | OpenAI GPT-4.1-mini |
| Infra      | AWS EC2, Docker |
| Database   | MySQL |
| Tools      | GitHub, Slack, Trello |

<img width="528" height="327" alt="Image" src="https://github.com/user-attachments/assets/06d79f2c-8cb1-47da-9da6-65cfcdecf05f" />


##  주요 기능
- 🧾 **자연어 지출 입력 → JSON 구조화**  
  `“6월 5일 스타벅스 5300원” → {"date": "2024-06-05", "category": "식비", "amount": 5300, "memo": "스타벅스"}`  

- 📊 **AI 소비 분석 리포트**  
  - 총 소비 / 카테고리별 지출 비율  
  - 예산 대비 소비율  
  - 주차별 소비 패턴 분석  
  - 개선 피드백 자동 제공  

- 📅 **월별 리포트 생성 / 조회 기능**  



##  서비스 화면
<p align="center">
  <img width="445" height="311" alt="Image" src="https://github.com/user-attachments/assets/425d27ee-5068-4a74-9d48-a4a6038f0bd6" />
  <img width="507" height="308" alt="Image" src="https://github.com/user-attachments/assets/68b90ed4-0671-46f6-a5c5-48fb129b1ee5" />
</p>


##  배포 및 성능 개선
- **멀티 스테이지 Docker 빌드** 적용 → 이미지 크기 `1.44GB → 733MB (약 49% 감소)`  
- **Spring Boot CORS 문제 해결** → `WebMvcConfigurer` 설정으로 프론트와 정상 통신  
- AWS EC2 환경에서 안정적으로 서비스 배포  



## 🔗 링크
- [GitHub - Backend](https://github.com/gk-adventure/Backend)  
- [GitHub - LLM](https://github.com/gk-adventure/LLM)  
