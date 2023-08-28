# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 김성진
- 리뷰어 : 황규빈


# PRT(PeerReviewTemplate) 
각 항목을 스스로 확인하고 토의하여 작성한 코드에 적용합니다.

- [ ] 코드가 정상적으로 동작하고 주어진 문제를 해결했나요?
  > 넵, 각 단계별로 구분을 지어 데이터로드, 전처리, 토큰화, 모델 설계 및 학습,
    평가 프로세스를 완벽히 수행하였습니다.
  > 데이터를 직접 확인하고 찾아가는 과정이 보이는게 너무 좋았습니다.
- [ ] 주석을 보고 작성자의 코드가 이해되었나요?
  > 단계별로 구분을 지어 이해하기 좋았습니다. 그리고 특히나 좋았던 점은 단계가 시작 될 때
    해당 단계에서 필요한 로직을 함수화를 하여 미리 선언해서 정리된 모습이 코드 이해하기 좋았습니다.
- [ ] 코드가 에러를 유발할 가능성이 없나요?
  > 넵, 특이점은 보이지 않습니다.
- [ ] 코드 작성자가 코드를 제대로 이해하고 작성했나요?
  > 넵, 데이터 하나 하나 직접 보면서, 필요한 전처리를 파악하는 모습이 이해도가 높아 보입니다.
- [ ] 코드가 간결한가요?
  > 넵, 역할별로 함수화하여 간결하게 코드를 잘 작성했습니다.
  ```
    def tokenize_ko_sentence(sentence, tokenizer, stopwords):
        tokenized_sentence = tokenizer.morphs(sentence) # 토큰화
        stopwords_removed_sentence = [word for word in tokenized_sentence if not word in stopwords] # 불용어 제거
        return stopwords_removed_sentence
    def get_stopwords_ko():
        # 불용어 정의
        stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
        return stopwords
    def tokenize_ko(sentences, tokenizer):
        stopwords = get_stopwords_ko()
        tokenized_data = []
        for sentence in tqdm(sentences):
            tokenized_data.append(tokenize_ko_sentence(sentence, tokenizer, stopwords))
        return tokenized_data
  ```

# 예시
1. 코드의 작동 방식을 주석으로 기록합니다.
2. 코드의 작동 방식에 대한 개선 방법을 주석으로 기록합니다.
3. 참고한 링크 및 ChatGPT 프롬프트 명령어가 있다면 주석으로 남겨주세요.
```python
```

# 참고 링크 및 코드 개선
```python
```
