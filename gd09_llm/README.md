# AIFFEL Campus Online Code Peer Review
- 코더 : 김성진
- 리뷰어 : 최철웅


# PRT(Peer Review Template)
- [ ]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    
- [x]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
  주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - input과 target 데이터를 토큰화할 때 들어간 데이터를 표시해두었다.
      ```python
      sources_tokenized = self._tokenize_fn(sources, tokenizer)  # source
      examples_tokenized = self._tokenize_fn(examples, tokenizer)  # source + target
      ```
  
- [x]  **3. 에러가 난 부분을 디버깅하여 문제를 “해결한 기록을 남겼거나” 
  ”새로운 시도 또는 추가 실험을 수행”해봤나요?**
    - 다양한 foundation model을 가지고 학습시킬때 가용 메모리 내에서 학습시킬 수 있는 하이퍼파리미터를 찾아냄
      ```text
      - 'psyche/kogpt'
        - model max length: 128
        - batch size: 4
        - ...로 낮추었을 때, 메모리 부족 에러나지 않고 학습 진행 가능함
      ```
  
- [ ]  **4. 회고를 잘 작성했나요?**
    - 모델 학습때 OOM을 겪은 경험을 서술함
        ```text
        # 회고
        - OOM
          - 이것 때문에 시간을 너무 많이 소모했다.
          - 한번 발생하면 gc.collect(), torch.cuda.empty_cache() 로도 메모리 초기화가 되지 않는다.
          - 해결책을 찾지 못하고, 그럴때마다 커널을 다시 시작해야 해서 너무 번거로웠다.
        - 데이터셋
          - 긴 토큰을 잘라내고, 데이터 증강을 2배한 결과가 더 좋기는 했는데 결과가 과대적합이 아닌지 좀 의심스러웠다.
          - 팀원분이 여기에서는 과대적합을 염려하지 않아도 괜찮을거라고 했다.
          - 추가 데이터셋은 당연하지만 단순히 그냥 늘린다고 결과가 좋아지지는 않음을 확인했다.
        - 전체적으로 이번 프로젝트는 많이 방황하고 어떻게 해야할지 막막해서 어려웠다.
        ```
    - 모델 학습 중간에 나온 데이터에 대한 평가도 남김
        ```text
        이후 수치

        batch_size: 4
        500	3.074800
        1000	2.929700
        1500	2.773500
        2000	2.680000
        2500	2.603100
        3000	2.489200
        3500	2.413400
        4000	2.364600
        4500	2.300000
        5000	2.258700
        5500	2.185900
        수치는 훨씬 낮아지긴 했는데, 과적합이 된건 아닐런지...
        ```
    
- [x]  **5. 코드가 간결하고 효율적인가요?**
    -  GPU 메모리 관리를 위해 함수를 만듦
        ```python
        import torch
        import gc
        # Check for and set up GPU
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        def get_cuda_memory_summary():
            # Obtain and print GPU memory summary
            memory_summary = torch.cuda.memory_summary(device=device, abbreviated=False)
            print(memory_summary)
            
        def empty_cuda_cache():
            # Run your deep learning code on the GPU
            gc.collect()
            torch.cuda.empty_cache()
            torch.cuda.synchronize()
        ```

# 참고 링크 및 코드 개선
```
# 코드 리뷰 시 참고한 링크가 있다면 링크와 간략한 설명을 첨부합니다.
# 코드 리뷰를 통해 개선한 코드가 있다면 코드와 간략한 설명을 첨부합니다.
```
