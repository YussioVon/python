lsnrctl start
sqlplus /nolog <<EOF
connect / as sysdba
startup;
exit
EOF