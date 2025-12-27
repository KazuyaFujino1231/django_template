# django_template

Django REST Framework + PostgreSQL の最小サンプルです。Todo の CRUD API を 1 本用意しています。

## セットアップ
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

### 環境変数（例）
PostgreSQL をローカル/コンテナで動かす前提です。必要に応じて置き換えてください。
```bash
export POSTGRES_DB=django
export POSTGRES_USER=django
export POSTGRES_PASSWORD=django
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
```

## マイグレーションと起動
```bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

## API
- エンドポイント: `http://localhost:8000/api/todos/`
- 例:
  - GET `/api/todos/`
  - POST `/api/todos/` `{ "title": "Buy milk", "description": "2 bottles" }`
  - PATCH `/api/todos/1/` `{ "is_done": true }`

ブラウザからも DRF のブラウザブル API で操作できます。

## TODO
- Sphinx を導入して開発者向けドキュメントを自動生成できるようにする（Docstring を反映する形でHTML化）。
