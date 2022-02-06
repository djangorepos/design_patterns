#!/bin/bash 

NAME= ithelp21ru
BACKUP=/root/backup
FILES="
/var/www/ithelp21/ftp/public_html
/etc/
"
DB=wp_it_help21_db
USER=debian-sys-ithelp21ru
PASS=D6L64F4HAqp5K59jljLH

mysqldump -u $USER -p$PASS $DB | gzip -9 > $BACKUP/$NAME-`date +"%A"`.sql.gz
tar -czf $BACKUP/$NAME-`date +"%A"`.tar.gz $FILES 
