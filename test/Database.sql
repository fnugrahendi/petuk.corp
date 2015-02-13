
---# nambah user
CREATE USER 'gd_user_akunting'@'localhost' IDENTIFIED BY 'nyungsep';

GRANT ALL PRIVILEGES ON * . * TO 'gd_user_akunting'@'%' IDENTIFIED BY 'nyungsep' WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0 ;


--- nek ra ngene
CREATE USER 'gd_user_akunting'@'localhost' IDENTIFIED BY 'nyungsep';
GRANT ALL PRIVILEGES ON *.* TO 'gd_user_akunting'@'localhost' IDENTIFIED BY 'nyungsep' WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;


---# nambah kolom ALTER TABLE `gd_detail_bank_masuk` ADD `catatan` VARCHAR( 512 ) NOT NULL ;# 2 row(s) affected.
---# ALTER TABLE `gd_detail_kas_masuk` ADD `catatan` VARCHAR( 512 ) NOT NULL ;# 2 row(s) affected.
---# ALTER TABLE `gd_detail_kas_keluar` ADD `catatan` VARCHAR( 512 ) NOT NULL ;# 3 row(s) affected.
