## FFMPEG Example Commands

#### 1. Converting Files

	#Using default settings w/ default codec library
	ffmpeg -i /path/to/input /path/to/output

	#Specifying a codec library
	ffmpeg -i /path/to/input -c:v libx264 /path/to/output

	#Using constant rate factor (visually lossless)
	ffmpeg -i /path/to/input -c:v libx264 -crf 18 /path/to/output


#### 2. Transcoding Files for Streaming

	#Creating a webm file
	ffmpeg -i /path/to/input -c:v libvpx -crf 23 -b:v 1M -c:a libvorbis /path/to/output.webm #where -b:v is the max bitrate

	#Creating an H.264 file
	ffmpeg -i /path/to/input -c:v libx264 -crf 23 -strict -2 -pix_fmt yuv420p -movflags faststart /path/to/output.mp4

#### 3. Stream Mapping

	#Copy video stream and transcode audio stream
	ffmpeg -i /path/to/input -c:v copy -c:a aac -strict -2 /path/to/output.mp4

	#Remove audio
	ffmpeg -i /path/to/input -c:v copy -an /path/to/output.mp4 #audio null

	#Export audio and video to separate files
	ffmpeg -i /path/to/input -map 0:0 /path/to/output.mp4 -map 0:1 /path/to/output.wav #defaults to 16 bit pcm

#### 4. Time-Based Commands

	#Export sections of a video
	ffmpeg -i /path/to/input -ss 00:00:00 -to 00:00:30 -c:v libx264 /path/to/output #export first 30 seconds of a video

	#Export a single frame as an image
	ffmpeg -i /path/to/input -ss 00:00:14.435 -vframes 1 /path/to/output.png

	#Altering framerates / time bases
	ffmpeg -i /path/to/input -c:v libx264 -vf setpts=0.5*PTS /path/to/output.mp4

	# Alters the actual presentation time stamp so that the playback is 2x faster

	ffmpeg -i /path/to/input -c:v libx264 -vf setpts=2.0*PTS /path/to/output.mp4

	# Alters the presentation time stamp so the playback is 2x slower

#### 5. Image Manipulation

	#Scale
	ffmpeg -i /path/to/input -c:v libx264 -vf scale=1920:1080 /path/to/output.mp4 #w:h

	#Crop
	ffmpeg -i /path/to/input -c:v libx264 -vf crop=100:100:0:0 /path/to/output.mp4
	# will crop a video to 100x100 square starting in the top left corner (crop=w:h:x_start:y_start)

	#Chaining filters
	ffmpeg -i /path/to/input -c:v libx264 -vf scale=100:100,crop=100:100:0:0 /path/to/output.mp4

#### 6. Batch Processing

	#Batch process files
	for x in *.avi; do
		ffmpeg -i $x -c:v libx264 -strict -2 ${x%.avi}.mp4;
	done
