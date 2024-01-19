코드 리뷰 기능과 Git 서버저장소 관리 기능을 제공하는 웹 기반 코드 리뷰 시스템

Github, Gitlab 등에서는 PR, MR 단계에서 merge 단위로 리뷰가 가능하나
Gerrit은 코드 리뷰에 목적을 둔 솔루션으로 각 Commit 단위로 리뷰를 진행할 수 있는 것이 특징이다
- 집중된 리뷰
- 빠른 피드백
- 분산된 리뷰 부담 감소

8989 port 웹으로 접속 가능하다

SSAFY Gerrit
- 백업
	- 명령어로 폴더를 압축한 후 home 폴더에 생성된 압축 파일을 SCP, SFTP 등으로 내려 받을 수 있음
	- 유사시를 대비해 주기적인 백업을 권장
	- replication 설정으로 소스 코드는 gitlab에 저장되더라도 코드 리뷰의 history는 gerrit을 복구해야만 확인이 가능
```linux
[백업]
sudo systemctl stop gerrit
cd /opt && sudo tar -czvf ~/gerrit-backup.tar.gz gerrit
sudo systemctl start gerrit
[복구]
sudo systemctl stop gerrit
sudo mv /opt/gerrit /opt/gerrit-old
sudo tar -xzvf gerrit-backup.tar.gz -C /opt/
sudo systemctl start gerrit
```

//백업
sudo systemctl stop gerrit
cd /opt && sudo tar -czvf ~/gerrit-backup.tar.gz gerrit
sudo systemctl start gerrit

//복구
sudo systemctl stop gerrit
sudo mv /opt/gerrit /opt/gerrit-old
sudo tar -xzvf gerrit-backup.tar.gz -C /opt/
sudo systemctl start gerrit