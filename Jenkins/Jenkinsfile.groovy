pipeline {
    agent any

    stages {
        stage('Tests') {
            steps {
                sh  'pytest --junitxml build\\report.xml tests\\'
                junit 'build\\report.xml'
            }
        }
    }
}