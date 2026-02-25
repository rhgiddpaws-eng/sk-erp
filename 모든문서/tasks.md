# MOAVO Habit MVP Tasks

- 최종 갱신: 2026-02-21
- 기준 문서:
  - `모든문서/시작문서/프로젝트요구사항.txt`
  - `현재진행상황_2026-02-21.md`
  - `모든문서/시작문서/Agent작동방식.txt`
  - `D:/BBB WISHCAT PROGECT BBB2/Kindergarten-Transmission/AutoAgent/참조할문서-이미지-링크/*`
- 참고 갭:
  - UI OCR 결과가 비어 있음(`입력 이미지 수 0`) -> 실제 Figma/원본 리소스 확인 필요

## 체크 규칙 (Dual Checkbox)
- `- [x] [ ]`: 현재 진행중(활성)
- `- [ ] [x]`: 작업 완료
- `- [ ] [ ]`: 대기
- 동시에 활성(`첫 번째 체크`) 가능한 태스크는 1개만 유지
- 모든 신규/수정 코드에는 쉬운 한국어 주석 포함

## 필수 키(추후 값 입력)
- `OPENAI_API_KEY`
- `GOOGLE_OAUTH_CLIENT_ID`
- `APPLE_TEAM_ID`
- `APPLE_KEY_ID`
- `APPLE_PRIVATE_KEY_BASE64`
- `GOOGLE_PLAY_SERVICE_ACCOUNT_JSON_BASE64`
- `APPSTORE_SHARED_SECRET`
- `JWT_SECRET`
- `ENCRYPTION_KEY_BASE64`

## Phase 0. 공통 기반/부트스트랩
- [ ] [x] [main-agent|P0] T0001 `모든문서/tasks.md`를 A~L + dual-checkbox 형식으로 구성
- [ ] [x] [do-agent|P0] T0002 Flutter 모노레포 기본 구조 생성(`app`, `admin-web`, `packages/core`)
- [ ] [x] [server-agent|P1] T0003 서버 초기 골격 생성(`/api/v1`, Prisma, Docker, env 템플릿)
- [ ] [x] [main-agent|P1] T0004 `docs/`에 phase별 작업 근거 문서 누적 규칙 적용

## Phase A. 온보딩
- [ ] [x] [ui-agent|P1] T0101 온보딩 화면 3단 구성 및 첫 실행 플래그(Local DB) 설계
- [ ] [x] [ui-agent|P1] T0102 온보딩 애니메이션(Lottie) + 진동/사운드 동기 처리

## Phase B. 회원가입/로그인
- [ ] [x] [server-agent|P1] T0201 이메일 회원가입/로그인 API 및 JWT 발급
- [ ] [x] [server-agent|P1] T0202 Google/Apple OAuth 로그인 API 연결
- [ ] [x] [ui-agent|P1] T0203 Flutter 로그인 화면 + 소셜 로그인 버튼 플로우

## Phase C. 메인홈/습관 히트맵
- [ ] [x] [ui-agent|P1] T0301 홈 대시보드(오늘 습관, 연속일, 달성률) 기본 레이아웃
- [ ] [x] [do-agent|P1] T0302 월간 히트맵 위젯 + Local DB 집계 연동

## Phase D. 습관등록 UX
- [ ] [x] [ui-agent|P1] T0401 습관 생성/수정 폼(빈도, 시간, 카테고리) 구현
- [ ] [x] [do-agent|P1] T0402 생성 완료 시 홈/히트맵 실시간 반영 상태관리 연결

## Phase E. 습관기록/AI API 연동
- [ ] [x] [server-agent|P1] T0501 `POST /api/v1/ai/comment` OpenAI 프록시 API 구현
- [ ] [x] [do-agent|P1] T0502 습관 기록 작성 후 AI 코멘트 팝업 연동
- [ ] [x] [test-agent|P2] T0503 AI 호출 실패/타임아웃/쿼터 초과 예외 처리 검증

## Phase F. 습관데이터/통계/레벨업
- [ ] [x] [do-agent|P1] T0601 주간/월간 통계 계산 로직(Local DB 우선) 구현
- [ ] [x] [ui-agent|P2] T0602 레벨/뱃지/경험치 UI 및 레벨업 연출 구현

## Phase G. 상세습관설정
- [ ] [x] [ui-agent|P2] T0701 습관별 알림, 반복, 목표 난이도 설정 화면 구현
- [ ] [x] [do-agent|P2] T0702 상세설정 변경분을 로컬 저장소와 동기화

## Phase H. 전체설정
- [ ] [x] [ui-agent|P2] T0801 계정/알림/언어/개인정보 설정 화면 구성
- [ ] [x] [do-agent|P2] T0802 i18n 리소스 구조(ko 기본 + 다국어 확장 슬롯) 적용

## Phase I. 위젯
- [ ] [x] [do-agent|P1] T0901 Android 홈 위젯 4단계 상태 전환(로컬 시간/로컬 DB)
- [ ] [x] [do-agent|P1] T0902 iOS WidgetKit TimelineProvider 기반 상태 전환
- [ ] [x] [test-agent|P1] T0903 18:00/22:00 전환 시나리오 및 배터리 영향 점검

## Phase J. 관리자페이지
- [ ] [x] [server-agent|P2] T1001 관리자 인증/권한 분리(`admin` role) 및 보호 미들웨어
- [ ] [x] [ui-agent|P2] T1002 관리자 웹(`admin-web`) 사용자/구독/AI 로그 조회 화면
- [ ] [x] [server-agent|P2] T1003 `POST /api/v1/admin/paywall-rules` 규칙 저장 API

## Phase K. 유료구독/결제
- [ ] [x] [do-agent|P1] T1101 Google/Apple IAP 구독 구매 플로우 구현
- [ ] [x] [server-agent|P1] T1102 영수증 검증 API(`verify/google`, `verify/apple`) 구현
- [ ] [x] [do-agent|P1] T1103 유료/무료 Paywall 차단 및 블러 처리 로직 구현

## Phase L. 계정연동/구매복원/오류절차/회원탈퇴
- [ ] [x] [server-agent|P1] T1201 `GET /entitlement`, `POST /restore`, `DELETE /account` 구현
- [ ] [x] [do-agent|P1] T1202 Flutter 구매복원 UI/실패 재시도 UX 구현
- [ ] [x] [test-agent|P1] T1203 탈퇴/복원/결제 오류 통합 회귀 테스트
