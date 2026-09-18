import argparse
from src.detector import HelmetDetector
from src.image_processor import process_image
from src.video_processor import process_video
from src.webcam_processor import process_webcam


def build_parser():
    parser = argparse.ArgumentParser(
        description="Smart Vision - Helmet Detection System"
    )
    sub = parser.add_subparsers(dest="mode", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--model", default="yolo11n.pt")
    common.add_argument("--confidence", type=float, default=0.40)

    image = sub.add_parser("image", parents=[common])
    image.add_argument("--input", required=True)
    image.add_argument("--output", default="data/output/detected_image.jpg")

    video = sub.add_parser("video", parents=[common])
    video.add_argument("--input", required=True)
    video.add_argument("--output", default="data/output/detected_video.mp4")

    webcam = sub.add_parser("webcam", parents=[common])
    webcam.add_argument("--camera", type=int, default=0)

    return parser


def main():
    args = build_parser().parse_args()
    detector = HelmetDetector(args.model, args.confidence)

    if args.mode == "image":
        process_image(detector, args.input, args.output)
    elif args.mode == "video":
        process_video(detector, args.input, args.output)
    elif args.mode == "webcam":
        process_webcam(detector, args.camera)


if __name__ == "__main__":
    main()
