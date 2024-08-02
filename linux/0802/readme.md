## 셸 스크립트

### 셸이란?
명령어 해석기; 셸은 사용자와 커널 사이에서 중계자 역할을 수행하는 프로그램   
Linux에는 본셸(Bourne shell; sh 명령어), C셸(C shell), korn shell, *bash shell*

### 셸스크립핑
명령어를 순서대로 시행되도록 코딩하여 자동화함

nano cmd
{   
nano $1   
chmod u+x $1   
./$1   
}  

./cmd test4 를 입력하면   
nano test4가 샐행되고 종료하면 자동으로 u+x 실행파일로 변경되고 실행이됨   

