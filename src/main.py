try:
    from ui.window import build_app
except ModuleNotFoundError:
    from src.ui.window import build_app


def main() -> None:
    root = build_app()
    root.mainloop()


if __name__ == "__main__":
    main()
