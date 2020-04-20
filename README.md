# AI_Automation


##### How to run this app
```sh
 git clone https://github.com/Sghosh1999/AI_Automation.git
 pip install -r requirements.txt
 streamlit run app.py
```

##### Code for setup.sh (Alternate with no credentials.toml)
```sh
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```


##### Code For Procfile
```sh
web: sh setup.sh && streamlit run app.py
```
