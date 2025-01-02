### Build and Run ANTLR4 to generate required parser files at `antlr-output`

```sh
git clone https://github.com/antlr/antlr4.git
```

```$
docker build -t antlr/antlr4 --platform linux/amd64 antlr4/docker

docker run --rm -u $(id -u ${USER}):$(id -g ${USER}) -v "$(pwd):/work" antlr/antlr4 -Dlanguage=Python3 -o antlr_output/ -visitor stellaris.g4
```

# Run the Tech Extractor
##### First set the enviroment variables
Copy `.env.example` and paste as `.env`, change the contents as needed.

##### Install dependencies
```sh
pip install -r requirements.txt
```

##### Run the script
```sh
py exportTechs.py
```

Output file: `exported_techs.json`
