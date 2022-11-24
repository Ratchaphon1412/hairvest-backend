FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add git zsh vim 
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
RUN pip install mysqlclient  

RUN apk del build-deps   

RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k &&  echo "source ~/powerlevel10k/powerlevel10k.zsh-theme" >>~/.zshrc
# setup shell
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
RUN git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
### Set ~/.zshrc in interactive terminal
### For powerlevel10K, Run Docker with TERM=xterm-256color
### docker run --rm -it -e "TERM=xterm-256color" /bin/bash

WORKDIR /root/backend
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 8000 5000
CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]