pipeline {
    agent any

    stages {
        stage('Tests') {
            steps {
                powershell  'python3 -m pytest --junitxml build\\report.xml tests\\'
                junit 'build\\report.xml'
            }
        }
    }
}