-- 개발용 초기 데이터 시드
-- 실행: psql -U cowork_user -d cowork_db -f seeds/initial_data.sql

-- 테스트 워크스페이스
INSERT INTO workspaces (id, name, slug, owner_id)
VALUES (
    uuid_generate_v4(),
    '개발팀 워크스페이스',
    'dev-team',
    (SELECT id FROM users LIMIT 1)
) ON CONFLICT DO NOTHING;
