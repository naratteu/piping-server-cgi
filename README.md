# piping-server-cgi
Piping Server Alternative for Classic Hosting Services

---

[nwtgck/piping-server](https://github.com/nwtgck/piping-server)를 구형 호스팅 서비스에서 운영하기 위한 대안입니다. 인터페이스나 기능이 호환되지는 않습니다.

## Transfer

You can transfer as follows.

```diff
# Send
-echo 'hello, world' | curl -T - https://ppng.io/hello
+echo 'hello, world' | curl -T - -X POST naratteu.woobi.co.kr/ppng.cgi?hello
```

```diff
# Get
-curl https://ppng.io/hello > hello.txt
+curl naratteu.woobi.co.kr/ppng.cgi?hello > hello.txt
```

테스트한 호스팅 서비스가 `GET`과 `POST`만 허용한 관계로 암시적으로 `PUT`요청을 할수가 없었습니다.

## Todo?

- piping-server-php