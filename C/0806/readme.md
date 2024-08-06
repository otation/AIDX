### C언어 제어문까지 배우기

#### 설치
Dev C++
mycompiler  

#### 변수 variables
변수를 만드려면 data type이 있어야 합니다.   
data type자료형  
char   1   -128 ~ 127 (signed)  / 0~255 (unsigned)
short  2   -32768 ~ 32767  
int    3   -2147483648 ~ 2147483647  
long   4   -9223372036854775808 ~ 9223372036854775807  

float  4   -3.4*10^38
double 8   -1.7*10^308

#### 산술연산자
#include <stdio.h>

int main() {
    int i, j;
    printf("정수 2개 입력 :");
    scanf("%d%d",&i,&j);
    printf("%d + %d = %d\n",i ,j, (i +j));
    printf("%d - %d = %d\n",i ,j, (i -j));
    printf("%d * %d = %d\n",i ,j, (i *j));
    printf("%d / %d = %.2f\n",i ,j, ((float)i /j));
    printf("%d %% %d = %d\n",i ,j, (i %j));
    return 0;
}

#### Shift연산자
#include <stdio.h>

int main() {
    int i, j;
    printf("정수 2개 입력 :");
    scanf("%d%d",&i,&j);
    printf("\n%d << %d = %d\n",i ,j, (i << j));
    printf("%d >> %d = %d\n",i ,j, (i >> j));
    return 0;
}











