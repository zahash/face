from face_recognition import load_image_file, face_encodings, face_locations
from os.path import abspath


def recognize(img_fpath):
    """
    Use the face_recognition library to detect all the faces
    in an image and calculate their corresponding encoding vectors
    and bounding box coordinates
    Args:
        img_fpath: the image path that may contains faces.
    Returns: An list that contains each face's filepath, location and encoding vector
    """
    image = load_image_file(img_fpath)
    encodings = face_encodings(image)
    bounding_boxes = [
        {"x1": loc[3], "y1": loc[0], "x2": loc[1], "y2": loc[2]}
        for loc in face_locations(image)
    ]  # loc = (y1, x2, y2, x1)

    faces = [
        {
            "img_fpath": abspath(img_fpath),
            "bounding_box": bounding_box,
            "face_encoding": face_encoding.tolist(),
        }
        for bounding_box, face_encoding in zip(bounding_boxes, encodings)
    ]

    return faces
