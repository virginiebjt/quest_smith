
Aller au contenu
Utiliser Gmail avec un lecteur d'écran
Meet
Nouvelle réunion
Rejoindre une réunion
Hangouts
2 sur 2
quest raspberry projet
Boîte de réception
Virginie B <vbejot@gmail.com>
	
Pièces jointesven. 31 juil. 2020 20:40
	
À moi
<?php
require __DIR__ . '/vendor/autoload.php';
use Mike42\Escpos\Printer;
use Mike42\Escpos\EscposImage;
use Mike42\Escpos\PrintConnectors\CupsPrintConnector;
$connector = new CupsPrintConnector("ZJ-58");
$printer = new Printer($connector);



$_GET = array();

foreach($argv as $key => $pair) {
    if ($key == 0) { //skip first element which is script name (test.php)
        continue;
    }

    list($key, $value) = explode(":", $pair);
    $_GET[$key] = $value;
    print $key;
    print $value;
}

$img_file = "/home/pi/quest_smith/story_text/".$_GET["story_follow_up"];

$myfile = fopen($img_file.".png", "r") or die("Unable to open file!");
$section = EscposImage::load($img_file.".png", "rb");

//$section = fread($myfile,filesize($text_file.".txt"));

  //  $tux = EscposImage::load("resources/tux.png", false);


fclose($myfile);


$printer -> bitImage($section);
$printer -> cut();
$printer -> close();

4 pièces jointes
	
	
	

import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

button = "none"
last_button_pressed_time= time.time()
story_follow_up = str("0")

subprocess.call(["php","-f","/home/pi/quest_smith/print.php","story_follow_up:"+str(story_follow_up)])

def leftButton(channel):
  global last_button_pressed_time 
  global button 
  global story_follow_up
  print("Button 1 pressed!")
  button = "left"
  current_time = time.time()
  time_passed_since_the_last_click = current_time - last_button_pressed_time
  last_button_pressed_time= current_time
  print(time_passed_since_the_last_click)
  if time_passed_since_the_last_click>5:
    story_follow_up += str("1")
    story_goes_on(1)

def rightButton(channel):
  global last_button_pressed_time 
  global button 
  global story_follow_up
  print("Button 2 pressed!")
  button = "right"
  current_time = time.time()
  time_passed_since_the_last_click = current_time - last_button_pressed_time
  last_button_pressed_time= current_time
  print(time_passed_since_the_last_click)
  if time_passed_since_the_last_click>5:
    story_follow_up += str("0")
    story_goes_on(0)

def story_goes_on(button):
  subprocess.call(["php","-f","/home/pi/quest_smith/print.php","story_follow_up:"+str(story_follow_up)])

GPIO.add_event_detect(23, GPIO.RISING, callback=leftButton, bouncetime=300)
GPIO.add_event_detect(24, GPIO.RISING, callback=rightButton, bouncetime=300)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up


push3.py
Affichage de printphpmarche.php en cours...
