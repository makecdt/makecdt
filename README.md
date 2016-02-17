# Chimerical
### [Devpost](http://devpost.com/software/chimerical-ataraxia#updates)
### [Website](http://makecdt.com/makecu/)

## Inspiration
<p>
Most patients that suffer from harsh brain trauma (a 3 or lower of the Glasgow Coma Scale) are considerably emotionally, mentally, and physically debilitated. Loss of neurological function, motor function, and emotional connection are common traits among such patients. The technology and current treatments usually costs thousands of dollars and require countless visits to the hospital with only short intermittent bursts of alleviation and direct assistance. This causes the process to take much longer and allow for inconsistencies to arise in regards to healing. With modern technological advancements and the integration of IoT, we strongly believe that we have developed an intriguing and useful home-based, modular product to help trauma patients recover and regain the stability they are progressing towards.
</p>
## What it does
<p>
Our application inter-operably integrates a neurological sensor (Muse) with a spatial and gesture recognition system (Myo) in order to provide the functionality equivalence of a small-scale EEG machine and muscle detection/analysis device. It seamlessly pairs two portable, intricate apparatuses to form a simple to operate system that takes above-mentioned measurements (and many more) to diagnose a patients cognitive and motor capabilities. The patient is able to use this product anywhere and anytime they wish to and because of it's compact, home-use design, it allows this to be marketed and as an off-the-shelf type of commodity. In more technical regards, our product combines the use of measuring brain waves (alpha, beta, delta, gamma) and muscle contraction to identify certain issues/advantages in the patients recovery process. From the data that these devices pull, we can extract binding senses, cognition, information processing, learning, perception, deep/REM sleep, conscious focus, memory, problem solving, relaxation, creativity, emotional connection, intuition, relaxation, and how well the patients muscle and skeletal systems operate. The most interesting keystone to this is the machine learning capability that over time will better understand the patients medical complications and thus have better technical accuracy and judgement in possible diagnoses and suggestions. If the patient experiences certain issues that are detected by the application or notable progresses, it will use Twilio to send an SMS to the primary physician. We also used Google maps in case you wanted to use our applications built-in route features to get to the destination.
</p>

## How we built it
<p>
We used Muse headband to measure neurological function and consistently stream that data through an AWS server to a horizontally scalable database (MongoDB), which allows to add future IoT devices and more amounts of data to our product. Likewise with the Myo, we allowed for such capabilities with respect to its own functionalities. We attempted to use TensorFlow for ML by analyzing the CSV data.
</p>

## Challenges we ran into
<p>
Incorporating TensorFlow was difficult with time limit and originally attempting to process the CSV data through an IoT device caused many hardware to hardware communication issues.
</p>

## Accomplishments that we're proud of
<p>
We actually got an enormous portion of work done. Scrum 4 #life.
</p>

## What we learned
<p>
How to use the Muse, Myo, and Servo on the spot and then have them inter-operably communicate with each other.
</p>

## What's next for Chimerical
<p>
Getting it to work at its full capacity and integrate all original features.
</p>
