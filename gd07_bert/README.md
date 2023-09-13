# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 김성진
- 리뷰어 : 리뷰어의 이름을 작성하세요.


# PRT(Peer Review Template)
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 토크나이징부터 MLM과 NSP task 데이터 생성까지 이루어졌다
    - 제시된 시각 자료를 통해 MLM loss와 NSP loss가 감소됨을 확인했다
        - ![image](https://github.com/knachinen/aiffel_goingdeeper/assets/12878951/d60d649f-7ade-4672-8dd3-f78ab094a288)
    - 학습시 loss값과 정확도의 변화를 그래프로 제시하였다
    
- [x]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
  주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 함수와 클래스에 파라미터와 반환값에 대해 설명하였다
      ```python
      class Preprocessor:
        def __init__(self, vocab, corpus_filepath, pretrain_filepath, 
                     n_seq=64, min_seq=8, max_mask=0.15,
                     verbose=False):
            """
            :param vocab: vocab (sentencepiece)
            :param corpus_filepath: input file path
            :parm pretrain_filepath: output json file path
            :param n_seq
            :param min_seq
            :param max_mask
            """
            self.vocab = vocab
            self.make_vocab_list()
            
            self.n_seq = n_seq
            self.min_seq = min_seq
            self.max_seq = n_seq - 3
    
            self.corpus_filepath = corpus_filepath
            self.pretrain_filepath = pretrain_filepath
      ```
  
- [x]  **3. 에러가 난 부분을 디버깅하여 문제를 “해결한 기록을 남겼거나” 
  ”새로운 시도 또는 추가 실험을 수행”해봤나요?**
    - 데이터 전처리 과정을 클래스화 하였다.
        - In \[76\]
            | 클래스화해서 데이터셋 만든 결과가 다르다...
            | 처리과정에서 뭔가 오류가 있는 것 같다.
            | 오류를 찾기에는 시간이 없어서 기존 함수를 재사용.
  
- [x]  **4. 회고를 잘 작성했나요?**
    - 학습 결과에 대해 스스로 분석하고 이를 기록하였다.
        - In \[113\]
            | t2: 전처리과정에서 함수를 클래스화를 했는데, 결과가 이상하게 나왔다.
            | loss 값은 이전보다 훨씬 낮은데, 수치 변동이 없는 것을 보면 학습이 제대로 되지 않는 것 같다.
            | t3: 원래대로 전처리 함수를 다시 사용하여 데이터셋을 만들면, nsp loss 값은 훨씬 높지만 학습은 진행되는 것처럼 보인다.
    
- [x]  **5. 코드가 간결하고 효율적인가요?**
    - 데이터셋을 MLM 및 NSP task화하는 과정을 클래스로 만들어 단순화함
      ```python
      preprocessor = Preprocessor(vocab, corpus_filepath, pretrain_filepath, max_mask=0.15)
      ```


# 참고 링크 및 코드 개선
`Preprocessor.make_pretrain_data()`를 정의하신 곳에서 버그를 발견했습니다.
```python
# ...
    def make_pretrain_data(self):
        """pretrain 데이터셋 생성"""
                
        # line count 확인
        line_cnt = 0
        with open(self.corpus_filepath, "r") as in_f:
            for line in in_f:
                line_cnt += 1

        with open(self.corpus_filepath, "r") as in_f:
            with open(self.pretrain_filepath, "w") as out_f:
                doc = []
                for line in tqdm(in_f, total=line_cnt):
                    line = line.strip()
                    if line == "":  # line이 빈줄 일 경우 (새로운 단락)
                        if 0 < len(doc):
                            self.save_pretrain_instances(out_f, doc)
                            doc = []
                    else:  # line이 빈줄이 아닐 경우 tokenize 해서 doc에 저장
                        pieces = self.vocab.encode_as_pieces(line)
                        if 0 < len(pieces):
                            doc.append(pieces)
                if 0 < len(doc):  # 마지막에 처리되지 않은 doc가 있는 경우
                    self.save_pretrain_instances(out_f, doc) # here
                    doc = []
```
마지막에 처리되지 않은 doc을 처리하는 과정에서 `save_pretrain_instances`를 호출하실때 `self`가 빠져있었습니다.
이 부분때문에 처리가 되지 않았는지는 모르겠지만 도움이 되었으면 좋겠습니다.
