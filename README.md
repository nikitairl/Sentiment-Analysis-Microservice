# Sentiment Analysis Microservice

<p align="center">
  <img src="https://downloader.disk.yandex.ru/preview/a1450b886faf2fdae9cf58a112ea53a3bc8063f2e39d3eee7c3f8dff22232eec/65baa090/c0xTB-RlQ9g8O1Auc5Khw6utgLAm4b-ji7PtPaXBqvakiLlJMCPCCCFOEJiUE_YK-KJb1j1vitB4uf_PiioS8Q%3D%3D?uid=0&filename=logo.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1722x1281" alt="Sentiment Analysis Microservice">
</p>

## Описание

Этот микросервис предоставляет API для определения настроения сообщения. Он использует модель машинного обучения для анализа текста и возвращает результат в форме позитивного, негативного или нейтрального настроения.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/nikitairl/Tone_check.git
   ```

2. Перейдите в каталог проекта:

   ```bash
   cd Tone_check

   ```

3. Запустите docker-compose:

   ```bash
   docker-compose up
   ```

## Использование

После успешного запуска микросервис будет доступен по следующему адресу:

```
http://localhost:8080
```

Вы можете отправить POST-запрос по эндпойнту `/predict_sentiment` с телом запроса в формате JSON:

```json
{
  "text": "Ваш текст для анализа настроения"
}
```

## Ответ

Микросервис вернет ответ в формате JSON:

```json
{
  "Настроение": "настроение",
  "Текст": "текст",
  "Точность": "значение"
}
```

Возможные значения для поля `Настроение`: "positive", "negative", "neutral".

## Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. в файле `LICENSE`.
