lsnrctl stop
sqlplus /nolog <<EOF
connect / as sysdba
shutdown immediate;
exit
EOF