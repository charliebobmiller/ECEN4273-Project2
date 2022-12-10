from pytest import mark
import os



class TestFiles:
    def test_fail(self):
        assert 1 == 0

    def test_pass(self):
        assert 0 == 0

    @mark.skip("skip")
    def test_skip(self):
        pass
        
    def check_single_file(testname, filename, expected_result):
        os.system('python3 ./yolov5/detect.py --weights ../yolov5/best.pt --source ../yolov5/data/images/zidane.jpg --save-txt')
        
        
    def test_cat(self):
        os.system('python3 ./yolov5/detect.py --weights ./yolov5/best.pt --source ./tests/test_images/cat.jpg --save-txt')
        f = open('./yolov5/runs/detect/exp/labels/cat.txt','r')
        result = f.read(1)
        os.system('rm -vr ./yolov5/runs/detect/exp')
        assert int(result) == 0  
                
    def test_dog(self):
        os.system('python3 ./yolov5/detect.py --weights ./yolov5/best.pt --source ./tests/test_images/dog.jpg --save-txt')
        f = open('./yolov5/runs/detect/exp/labels/dog.txt','r')
        result = f.read(1)
        os.system('rm -vr ./yolov5/runs/detect/exp')
        assert int(result) == 1

    def test_multirotor(self):
        os.system('python3 ./yolov5/detect.py --weights ./yolov5/best.pt --source ./tests/test_images/multirotor.jpg --save-txt')
        f = open('./yolov5/runs/detect/exp/labels/multirotor.txt','r')
        result = f.read(1)
        os.system('rm -vr ./yolov5/runs/detect/exp')
        assert int(result) == 2

    def test_person(self):
        os.system('python3 ./yolov5/detect.py --weights ./yolov5/best.pt --source ./tests/test_images/person.jpg --save-txt')
        f = open('./yolov5/runs/detect/exp/labels/person.txt','r')
        result = f.read(1)
        os.system('rm -vr ./yolov5/runs/detect/exp')
        assert int(result) == 3

    def test_pikachu(self):
        os.system('python3 ./yolov5/detect.py --weights ./yolov5/best.pt --source ./tests/test_images/pikachu.jpg --save-txt')
        f = open('./yolov5/runs/detect/exp/labels/pikachu.txt','r')
        result = f.read(1)
        os.system('rm -vr ./yolov5/runs/detect/exp')
        assert int(result) == 5

