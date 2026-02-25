# Kindergarten Transmission Project Tasks

## Phase 1: Planning & Analysis
- [x] 에듀파인 분석 및 수행 범위 정의
- [x] 분석 기반 상세 기획 (요구 사항 정의, 기능 정의, 화면 설계 등)
- [x] UI/UX 디자인 가이드 완성 (벤치마킹: DMB iCube)
- [x] 상세 기능 요구 사항 구성

## Phase 2: Infrastructure & Schema
- [x] 서버/DB/인프라 구성 (docker-compose postgres 구성)
- [x] 웹 기반 시스템 완성을 위해 Next.js 15, Tailwind CSS 4, postgresql-prisma 스키마 작성

## Phase 3: Core Implementation
- [x] 구현: 시스템 관리자 기능 (내부 직원 계정 관리, 권한 관리 등)
- [x] 구현: 고객사(유치원) 관리 (유치원별 정보 등록, 에듀파인 접속 정보 보안 저장 등)
- [x] 구현: 전표 입력 및 관리 (수입/지출 결의서 작성, 계정 과목 설정)
- [x] 구현: 데이터 매핑 (시스템 영역 데이터를 에듀파인 일괄 양식으로 변환)
- [x] 구현: 은행 계좌 스크래핑 백엔드 (빠른계좌조회 연동 및 내역 파싱)
- [x] 구현: 자동 전송/등록 (Playwright RPA 연동)

## Phase 4: Verification & Mobile
- [x] 테스트: 전송 결과 확인 (성공/실패 여부 피드백)
- [x] 구현: PC Web 버전을 모바일로 컨버팅 후 기능 작동 확인
