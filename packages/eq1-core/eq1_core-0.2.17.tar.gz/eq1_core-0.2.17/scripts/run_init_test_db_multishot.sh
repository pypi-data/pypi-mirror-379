#!/bin/bash

# UV를 사용하여 multishot 테스트 DB 초기화 스크립트 실행
# 실행 방법: ./scripts/run_init_test_db_multishot.sh

echo "🚀 UV를 사용하여 multishot 테스트 DB 초기화를 시작합니다..."

# 프로젝트 루트로 이동
cd "$(dirname "$0")/.."

# UV를 사용하여 스크립트 실행
uv run scripts/init_test_db_multishot.py

echo "✅ 스크립트 실행이 완료되었습니다."
