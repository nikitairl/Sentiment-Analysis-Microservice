# Sentiment Analysis Microservice

<p align="center">
  <img src="https://downloader.disk.yandex.ru/preview/68aad220c7a8c5421488883f0b043ba19c660bd8044e8bd47834ac2349f0d2a9/65baa1ff/IEu4thWZ5QKeK8ya-wsbVIOxDNWJaLVvqxarU8gM_jUJjNjY6o8EkZKDsHuw5Mm8BO82Gj-2Yuvm67GxDFqLnw%3D%3D?uid=0&filename=00053-1901053811.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1722x1281">
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
