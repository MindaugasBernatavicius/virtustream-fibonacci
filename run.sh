sudo service nginx restart
if [ $? -eq 0 ]; then
    uwsgi config/vs-fib.ini
else
    echo "Nginx failed to start!"
fi