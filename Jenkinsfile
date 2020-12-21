pipeline {
    agent any

    stages {
        stage ('Checkout'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github_creds', url: 'https://github.com/Frodan/sna_final.git']]])
            }
        }
        stage('Build') {
            steps{
                echo 'build stage'
                git branch: 'main', url: 'https://github.com/Frodan/sna_final.git'
                sh "pip3 install -r requirements.txt"
            }

        }
        stage('Test'){
            steps{
                echo "test stage"
                sh "python3 test.py"
            }
        }
        stage('Deploy'){
            steps{
                echo "deplooooy"
                sh "ls /home/ubuntu"
                //sh "ssh -i /home/ubuntu/NotVeryWell.pem ubuntu@172.31.42.233 date"
            }
        }
    }
}
