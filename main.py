# Audios imports
from audios.audio_templates import audio_templates as at
from voice_generate.app import voice
from voice_recognition.app import reconhecimento_audio
from pydub import AudioSegment
from pydub.playback import play
# Face recognition imports
import face_recognition
import cv2
import numpy as np
import os
from pathlib import Path
# Chat imports
from api_alice_online.googlebardapi import GoogleBard

# Audio constants
AUDIO_PATH = './audios/'
WELCOME = 'welcome'
FACE_RECOGNITION_INSTRUCTIONS = 'face_recognition_instructions'
HELLO_MESSAGE_PART_1 = 'Olá '
HELLO_MESSAGE_PART_2 = '! No que posso te ajudar?'
TEMP_RESP_AUDIO = AUDIO_PATH + 'temp/resp.mp3'
SEARCHING = 'searching'
RESPONSE_INIT = 'response_init'

# Face recognition constants
FACES_PATH = './face_recognition/known/'
faces_files_known = os.listdir(FACES_PATH)
faces_names_known = []
i = 0
while(i < len(faces_files_known)):
    faces_names_known.append(Path(faces_files_known[i]).stem)
    faces_files_known[i] = FACES_PATH + faces_files_known[i]
    i += 1

def get_audio_template_info(message_key, item_key):
    return at().get(message_key).get(item_key)

def get_audio_template_text(message_key):
    return get_audio_template_info(message_key, 'text')

def get_audio_template_audio_name(message_key):
    return AUDIO_PATH + get_audio_template_info(message_key, 'audio_name')

def temp_voice_generate(text_print):
    voice(text_print, TEMP_RESP_AUDIO)

def play_voice_from_template(message_key):
    play_voice(get_audio_template_audio_name(message_key))

def play_voice(audio_file):
    play(AudioSegment.from_file(audio_file))

def main():
    # Welcome message and voice
    print('---------------------------')
    print()
    print(get_audio_template_text(WELCOME))
    play_voice_from_template(WELCOME)
    print()
    print(get_audio_template_text(FACE_RECOGNITION_INSTRUCTIONS))
    play_voice_from_template(FACE_RECOGNITION_INSTRUCTIONS)
    print()

    # start face recognition
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)

    known_face_encodings = []
    known_face_names = []

    for image, name in zip(faces_files_known, faces_names_known):
        # Load a sample picture and learn how to recognize it.
        image_loaded = face_recognition.load_image_file(image)
        face_encoding = face_recognition.face_encodings(image_loaded)[0]

        # Create arrays of known face encodings and their names
        known_face_encodings.append(face_encoding)
        known_face_names.append(name)

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    person_recognized_bool = False
    process_this_frame_person_recognized_number = 0
    skip_first_frame = True
    unknown_name = "Unknown"

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Variable to store the name of the first people recognized
        person_recognized = unknown_name

        # Only process every other frame of video to save time
        if process_this_frame:
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            # rgb_small_frame = small_frame[:, :, ::-1]
            
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = unknown_name

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

            for name in face_names:
                if name != unknown_name:
                    person_recognized = name
                    break

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1, cv2.LINE_8)
        

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Skip the first frame to avoid a dark panel
        if not skip_first_frame:
            # If a person is recognized, skip ten frames recognitions of video
            if not person_recognized_bool:
                if person_recognized != unknown_name:
                    person_recognized_bool = True
                    # Start the voice recognition
                    print()
                    text_print = HELLO_MESSAGE_PART_1 + person_recognized + HELLO_MESSAGE_PART_2
                    temp_voice_generate(text_print)
                    print(text_print)
                    play_voice(TEMP_RESP_AUDIO)
                    voice_command = reconhecimento_audio()
                    if(voice_command != ''):
                        print()
                        print('Sua pergunta: ' + voice_command)
                        print()
                        print('Pensando...')
                        response = GoogleBard(voice_command)
                        temp_voice_generate(response)
                        print()
                        print(response)
                        play_voice(TEMP_RESP_AUDIO)

                else:
                    person_recognized_bool = False
            else:
                if process_this_frame_person_recognized_number > 10:
                    process_this_frame_person_recognized_number = 0
                    person_recognized_bool = False
                else:
                    process_this_frame_person_recognized_number += 1
        else:
            skip_first_frame = False

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

main()
