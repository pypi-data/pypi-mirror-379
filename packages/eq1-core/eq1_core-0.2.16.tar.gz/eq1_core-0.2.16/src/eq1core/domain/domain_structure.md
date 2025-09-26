# domain structure

src/
├── domain/
│   ├── entities/                      # 도메인 엔티티 (순수 Python 객체)
│   │   ├── camera.py
│   │   ├── component.py
│   │   ├── component_result.py
│   │   ├── engine.py
│   │   ├── predictor.py
│   │   ├── product.py
│   │   ├── product_result.py
│   │   └── users.py
│   │
│   └── ports/                         # 추상 인터페이스 (Ports)
│       ├── camera_port.py
│       ├── component_port.py
│       ├── component_result_port.py
│       ├── engine_port.py
│       ├── predictor_port.py
│       ├── product_port.py
│       ├── product_result_port.py
│       └── users_port.py

├── infrastructure/
│   ├── api/                           # 외부 FastAPI 서버 연동용 Port 구현
│   │   ├── adapters/
│   │   │   ├── camera_api.py
│   │   │   ├── component_api.py
│   │   │   ├── component_result_api.py
│   │   │   ├── engine_api.py
│   │   │   ├── predictor_api.py
│   │   │   ├── product_api.py
│   │   │   ├── product_result_api.py
│   │   │   └── users_api.py
│   │   ├── client.py                  # 공통 HTTP 클라이언트 (requests wrapper)
│   │   └── factory.py                 # RepoFactory.from_api()

│   ├── db/                            # DB 기반 Port 구현
│   │   ├── models/                    # SQLAlchemy ORM 모델
│   │   │   ├── camera_model.py
│   │   │   ├── component_model.py
│   │   │   ├── component_result_model.py
│   │   │   ├── engine_model.py
│   │   │   ├── predictor_model.py
│   │   │   ├── product_model.py
│   │   │   ├── product_result_model.py
│   │   │   └── users_model.py
│   │   ├── repositories/              # DB Port 구현체
│   │   │   ├── camera_repo.py
│   │   │   ├── component_repo.py
│   │   │   ├── component_result_repo.py
│   │   │   ├── engine_repo.py
│   │   │   ├── predictor_repo.py
│   │   │   ├── product_repo.py
│   │   │   ├── product_result_repo.py
│   │   │   └── users_repo.py
│   │   ├── mappers/                   # ORM ↔ Entity 변환
│   │   │   ├── camera_mapper.py
│   │   │   ├── component_mapper.py
│   │   │   ├── component_result_mapper.py
│   │   │   ├── engine_mapper.py
│   │   │   ├── predictor_mapper.py
│   │   │   ├── product_mapper.py
│   │   │   ├── product_result_mapper.py
│   │   │   └── users_mapper.py
│   │   ├── session.py                 # SQLAlchemy 세션 관리
│   │   └── factory.py                 # RepoFactory.from_db()