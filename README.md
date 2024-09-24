## Team Park-to-Play: P2P
서울시 공연장 주변 주차장 추천 챗봇 프로젝트

<br>

### 소개
서울시 내에서 공연이나 축제와 같은 문화 행사를 방문하는 사람들이 주차 문제로 인한 불편을 겪지 않도록, 효율적인 주차장 추천 시스템을 개발하여 사용자가 신속하고 편리하게 적합한 주차장을 찾을 수 있도록 도와주는 챗봇 서비스를 개발하는 프로젝트입니다.


<br>

### 멤버
* [김관용](https://github.com/ToleranceKim)
* [김윤일](https://github.com/yunilkim)
* [서동옥](https://github.com/SeoDongOk)
* [이종찬](https://github.com/qkskfka)`
* [장준혁](https://github.com/JangJune)
* [최준혁](https://github.com/kimbap918)


<br>

## 목차 
[requirements.txt에 저장된 환경 설치하기](#requirements.txt에 저장된 환경 설치하기)

- [Windows에서 가상환경 생성 및 실행](#windows에서-가상환경-생성-및-실행)
	-  [Windows에서 장고(Django) 설치 및 환경설정](#windows에서-장고django-설치-및-환경설정)
- [MAC에서 가상환경 생성 및 실행](#mac에서-가상환경-생성-및-실행) 
	- [MAC 장고(Django) 설치 및 환경설정](#mac-장고django-설치-및-환경설정) 


# requirements.txt에 저장된 환경 설치하기
프로젝트 파일 내부에 있는 requirements.txt를 설치하여 개발환경을 동기화 시킵니다.

1. 현재 설치된 패키지를 `requirements.txt`에 저장하기
```bash
pip freeze > requirements.txt
```
2. 저장된 환경을 설치하기
``` bash
pip install -r requirements.txt
```


# Windows에서 가상환경 생성 및 실행

### 1. pyenv 설치 및 python 설치
* pyenv 설치하기
* pyenv는 여러 파이썬 버전을 쉽게 바꾸어 쓸 수 있게 도와줍니다.

```bash
git clone https://github.com/pyenv/pyenv.git %USERPROFILE%/.pyenv
```

* 환경변수 설정:

1) `내 컴퓨터 > 속성 > 고급 시스템 설정 > 환경 변수`로 이동  
2) 사용자 변수에 다음을 추가:

   * 변수 이름: `PYENV`
   * 변수 값: `%USERPROFILE%/.pyenv`

3) 시스템 변수에서 `Path`를 선택하고 편집을 클릭. `새로 만들기`를 클릭하고 `%PYENV%\bin` 추가 후 확인.

4) 명령 프롬프트에서 아래 명령을 실행해 환경 설정 완료:

```bash
pyenv install --version
```

<br>

### 2. python 설치하기

```bash
pyenv install -list
```

<br>

### 3. python 설치 및 설치 후 버전 확인하기
* 여기서는 3.11.9로 통일합니다.

```bash
pyenv install 3.11.9
pyenv versions 
```
![](https://i.imgur.com/pQl0VHQ.png)
새로 설치된 3.11.9

<br>

### 4. 실제 환경에서 사용할 버전 선택하기

```bash
$ pyenv shell 3.11.9
```
![](https://i.imgur.com/H4kcg3G.png)

<br>

### 5. virtualenv 설치
* 가상 환경을 생성하고 사용할 수 있도록 해줍니다.

```bash
git clone https://github.com/pyenv/pyenv-virtualenv.git %USERPROFILE%/.pyenv/plugins/pyenv-virtualenv
```

<br>

### 6. 가상 환경 생성하기

```bash
pyenv virtualenv [파이썬 버전] [가상 환경 이름]
pyenv virtualenv 3.11.9 p2p-env
```
가상환경의 이름은 임의로 생성해도 됩니다.

<br>

### 7. 가상 환경이 생성 되었는지 확인을 한다.

```bash
pyenv versions
```
![](https://i.imgur.com/SZUiWis.png)

<br>

### 8. 가상 환경 실행 명령

```bash
pyenv activate [가상 환경 이름]
pyenv activate p2p-env
```

### 8-1. 가상 환경 실행 오류 발생 시

1) 설정 파일을 열기  
   `C:\Users\<사용자명>\.pyenv\pyenv-win\version\pyenv.vbs` 파일을 텍스트 편집기로 엽니다.

2) 다음 내용을 추가:

```bash
export PATH="$HOME/.pyenv/bin:$PATH" 
eval "$(pyenv init --path)" 
eval "$(pyenv init -)" 
eval "$(pyenv virtualenv-init -)"
```

3) 명령 프롬프트를 다시 실행 후, 가상 환경을 다시 활성화

``` bash
pyenv activate p2p-env
```

<br>

### 9. 가상 환경 해제 명령

```bash
pyenv deactivate
```

<br>

## Windows에서 장고(Django) 설치 및 환경설정

### 1. 가상환경 실행

```bash
pyenv activate [가상 환경 이름]
pyenv activate p2p-env
```

<br>

### 2. 가상 환경 실행 후 django를 설치할 폴더를 생성하고 cd 명령을 통해 폴더로 이동
**주의할점 :** 현재 github의 P2P repository에는 이미 폴더가 생성 되어있어, P2P을 clone했다면 이 절차를 생략해야합니다. 다시 생성하면 안됩니다. 

```bash
mkdir [폴더명] (폴더가 생성되어 있다면 할 필요 없음)
cd [폴더명]


mkdir p2p
cd p2p
```

<br>

### 3. django 설치 전 pip upgrade

```bash
python3 -m pip install --upgrade pip
```

<br>

### 4. django 설치

```bash
pip install django
pip3 install django
```

<br>

### 5. 설치 확인

```bash
python -m django --version
python3 -m django --version
```
![](https://i.imgur.com/mebeugF.png)

<br>

### 6. 프로젝트 생성
**주의할점 :** 현재 github의 P2P repository에는 이미 폴더가 생성 되어있어, P2P을 clone했다면 이 절차를 생략해야합니다. 다시 생성하면 안됩니다. 
```bash
django-admin startproject [생성할 폴더명]
django-admin startproject p2p
```

<br>

### 7. 생성한 폴더로 이동 후 서버 실행
```bash
python3 manage.py runserver
python manage.py runserver
```
![](https://i.imgur.com/fmQsmUO.png)

<br>

### 완료
해당 절차를 수행했다면 로컬 서버 `http://127.0.0.1:8000/` 실행 시, 아래와 같은 화면이 출력됩니다. 이제 Django 프로젝트를 수행할 준비가 되었습니다.
![](https://i.imgur.com/SP8tlOI.png)





# MAC에서 가상환경 생성 및 실행

### 1. pyenv 설치 및 python 설치

* pyenv 설치하기
* pyenv는 여러 파이썬 버전을 쉽게 바꾸어 쓸 수 있게 도와줍니다.

```bash
brew install pyenv
echo 'eval "$(pyenv init -)"' >> /.bash_profile
```

<br>

### 2. python 설치하기

```bash
pyenv install -list
```

<br>

### 3. python 설치 및 설치 후 버전 확인하기
* 여기서는 3.11.9로 통일합니다.

```bash
pyenv install 3.11.9
pyenv versions 
```
![](https://i.imgur.com/pQl0VHQ.png)
새로 설치된 3.11.9


<br>

### 4. 실제 환경에서 사용할 버전 선택하기

```bash
$ pyenv shell 3.11.9
```
![](https://i.imgur.com/H4kcg3G.png)
<br>

### 5. virtualenv 설치
* 가상 환경을 생성하고 사용할 수 있도록 해줍니다.

```bash
brew install pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
```

<br>

### 6. 가상 환경 생성하기

```bash
pyenv virtualenv [파이썬 버전] [가상 환경 이름]
pyenv virtualenv 3.11.9 p2p-env
```
가상환경의 이름은 임의로 생성해도 됩니다.

<br>

### 7. 가상 환경이 생성 되었는지 확인을 한다.

```bash
pyenv versions
```
![](https://i.imgur.com/SZUiWis.png)

<br>

### 8. 가상 환경 실행 명령

```bash
pyenv activate [가상 환경 이름]
pyenv activate p2p-env
```


### 8-1. 가상 환경 실행 오류 발생 시
![](https://i.imgur.com/Qg50M7N.png)
만약, 위와 같은 오류가 발생한다면 다음 명령어를 따라해봅시다.


1) 설정 파일을 열기
``` bash
nano ~/.bash_profile  # 또는 nano ~/.zshrc
```
2) 다음 내용을 추가
```bash
export PATH="$HOME/.pyenv/bin:$PATH" 
eval "$(pyenv init --path)" 
eval "$(pyenv init -)" 
eval "$(pyenv virtualenv-init -)"
```
3) 변경 사항을 적용
4) 쉘 다시 시작
```bash
exec "$SHELL"
```
5) 가상 환경 다시 활성화
``` bash
pyenv activate p2p-env
```


<br>

### 9. 가상 환경 해제 명령

```bash
pyenv deactivate
```

<br>

## MAC 장고(Django) 설치 및 환경설정

### 1. 가상환경 실행

```bash
pyenv activate [가상 환경 이름]
pyenv activate p2p-env
```

<br>

### 2. 가상 환경 실행 후 django를 설치할 폴더를 생성하고 cd 명령을 통해 폴더로 이동
**주의할점 :** 현재 github의 P2P repository에는 이미 폴더가 생성 되어있어, P2P을 clone했다면 이 절차를 생략해야합니다. 다시 생성하면 안됩니다. 

```bash
mkdir [폴더명] (폴더가 생성되어 있다면 할 필요 없음)
cd [폴더명]


mkdir p2p
cd p2p
```

<br>

### 3. django 설치 전 pip upgrade

```bash
python3 -m pip install --upgrade pip
```

<br>

### 4. django 설치

```bash
pip install django
pip3 install django
```

<br>

### 5. 설치 확인

```bash
python -m django --version
python3 -m django --version
```
![](https://i.imgur.com/mebeugF.png)

<br>

### 6. 프로젝트 생성
**주의할점 :** 현재 github의 P2P repository에는 이미 폴더가 생성 되어있어, P2P을 clone했다면 이 절차를 생략해야합니다. 다시 생성하면 안됩니다. 
```bash
django-admin startproject [생성할 폴더명]
django-admin startproject p2p
```

<br>

### 7. 생성한 폴더로 이동 후서버 실행
```bash
python3 manage.py runserver
python manage.py runserver
```
![](https://i.imgur.com/fmQsmUO.png)


<br>

### 완료
해당 절차를 수행했다면 로컬 서버 `http://127.0.0.1:8000/` 실행 시, 아래와 같은 화면이 출력됩니다. 이제 Django프로젝트를 수행할 준비가 되었습니다.
![](https://i.imgur.com/SP8tlOI.png)



