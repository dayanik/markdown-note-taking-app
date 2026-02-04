# markdown-note-taking-app
реализована идея с минимальным функционалом с сайта [roadmap.sh](https://roadmap.sh/projects/markdown-note-taking-app).

## todo
- валидация файлов перед загрузкой
- валидация/экраниерование текста перед сохранением в файл
- выдача файла через nginx
## технологии
- `python3.14`
- `django6.0.2`
- `mistune` -- конвертация md -> html
- `language-tool-python>=3.2.2` -- проверка грамматики
- `docker`
- `nginx`
## Установка и настройка
Необходимо установить в систему docker, если нет.

1. Clone the repository and move into it:
```bash
git clone https://github.com/dayanik/markdown-note-taking-app
cd markdown-note-taking-app
```
2. Прописать переменные в .env
```bash
cp example.env .env
nano .env
```
3. Прописать доступные адреса хостов для django
```bash
nano mdnt_app/mdnt_app/settings.py
```

4. Install dependencies:
```bash
docker compose up -d --build
```