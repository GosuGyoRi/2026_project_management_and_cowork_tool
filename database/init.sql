-- 초기 DB 설정
-- Docker 컨테이너 최초 실행 시 자동 실행됩니다.

-- UUID 확장 활성화
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 실제 테이블 생성은 Alembic 마이그레이션으로 관리합니다.
-- 이 파일은 확장 설치 및 초기 설정만 담당합니다.
