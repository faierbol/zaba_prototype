# zaba_prototype
prototype ad site


python manage.py compilemessages


create fixture:
./manage.py dumpdata auth.user --indent 2 > user.json
./manage.py loaddata user.json
## docker
_if you use docker please change "localhost" to "redis" (REDIS_HOST = 'localhost')_

`docker-compose -f "docker-compose.yml" up -d --build`

On Linux for start Elasticsearch > v.5
`sysctl -w vm.max_map_count=262144
`

webpack build main.js 

`npm run dev`
