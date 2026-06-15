import os
import subprocess
import urllib.parse
import warnings
import flet as ft

# Hide system deprecation clutter to ensure a totally clean console window
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ==========================
# DARK PINK THEME PALETTE
# ==========================
BG = "#0D0006"          # Deep Midnight Maroon
CARD = "#1A000D"        # Dark Velvet Pink Card Body
PRIMARY = "#FF2D8A"     # Hot Neon Magenta
TEXT = "#FCE4EC"        # Light Pastel Rose Text
SUBTEXT = "#FF85B3"     # Soft Pink Accent Text
BORDER_COLOR = "#3D001F" # Subtle Pink-Tinted Border


# ==========================
# SAFE DIRECT FILE OPENER
# ==========================
def open_asset_file(relative_path):
    """
    Finds the file inside the local assets folder and opens it 
    natively using the standard Windows system shell.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    clean_path = urllib.parse.unquote(relative_path).lstrip("/")
    full_path = os.path.normpath(os.path.join(current_dir, "assets", clean_path))
    
    if os.path.exists(full_path):
        try:
            # Command line invocation ensures Windows doesn't lock up the main Flet thread
            subprocess.Popen(['start', '', full_path], shell=True)
            return f"✓ Opening: {os.path.basename(full_path)}"
        except Exception as e:
            return f"⚠ System Error: Could not launch file reader ({str(e)})"
    else:
        return f"⚠ File Not Found: Please check assets/ directory structure"


# ==========================
# UI COMPONENTS & BUILDERS
# ==========================
def section_title(title):
    return ft.Text(
        title,
        size=24,
        weight=ft.FontWeight.BOLD,
        color=PRIMARY,
    )


def skill_chip(skill):
    return ft.Container(
        content=ft.Text(skill, color=BG, weight=ft.FontWeight.BOLD),
        bgcolor=PRIMARY,
        border_radius=20,
        padding=10,
        margin=5,
    )


def timeline_step(milestone, title, details):
    return ft.Container(
        bgcolor="#260013",
        border_radius=12,
        padding=15,
        margin=ft.Margin(0, 0, 0, 8),
        border=ft.Border.all(width=1, color=BORDER_COLOR),
        content=ft.Row(
            [
                ft.Container(
                    content=ft.Text(
                        milestone, color=BG, weight=ft.FontWeight.BOLD, size=12
                    ),
                    bgcolor=SUBTEXT,
                    padding=ft.Padding(12, 6, 12, 6),
                    border_radius=8,
                ),
                ft.VerticalDivider(width=10, color="transparent"),
                ft.Column(
                    [
                        ft.Text(title, weight=ft.FontWeight.BOLD, color=TEXT, size=15),
                        ft.Text(details, color=SUBTEXT, size=13),
                    ],
                    expand=True,
                    spacing=2,
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def info_card(title, content):
    return ft.Container(
        bgcolor=CARD,
        border_radius=15,
        padding=20,
        border=ft.Border.all(width=1, color=BORDER_COLOR),
        content=ft.Column(
            [
                ft.Text(title, size=22, weight=ft.FontWeight.BOLD, color=PRIMARY),
                ft.Text(content, size=16, color=TEXT),
            ]
        ),
    )


# ==========================
# PORTFOLIO STAGE ASSEMBLY
# ==========================
def main(page: ft.Page):
    page.title = "Esra Tangi Kalola Portfolio"
    page.bgcolor = BG
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    page.theme_mode = ft.ThemeMode.DARK

    # Top Status Message Banner
    status_banner = ft.Container(
        content=ft.Text("", color=BG, weight=ft.FontWeight.BOLD, size=14),
        bgcolor=PRIMARY,
        padding=12,
        border_radius=10,
        visible=False,
    )

    def trigger_status_update(message):
        status_banner.content.value = message
        status_banner.visible = True
        page.update()

    # Click Interaction Triggers linked directly to system paths
    def launch_cert_file(path):
        result_msg = open_asset_file(path)
        trigger_status_update(result_msg)

    def launch_video_file(e):
        result_msg = open_asset_file("/projects/20260614_133818.mp4")
        trigger_status_update(result_msg)

    # Custom builder for the certificate cards
    def certificate_card(title, path):
        return ft.Container(
            width=280,
            bgcolor=CARD,
            border_radius=15,
            padding=20,
            border=ft.Border.all(width=1, color=BORDER_COLOR),
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.CARD_MEMBERSHIP, size=40, color=PRIMARY),
                    ft.Text(title, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD, color=TEXT),
                    ft.TextButton(
                        "Open Certificate PDF", 
                        on_click=lambda e: launch_cert_file(path),
                        style=ft.ButtonStyle(color=SUBTEXT)
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    # Registered Certificate Target Files Map
    certificate_data = [
        ("Calculations with Vectors and Matrices", "/certificates/calculations with vectors and matrices.pdf"),
        ("CORE MATLAB Skills", "/certificates/CORE MATLAB Skills.pdf"),
        ("Explore Data with MATLAB Plots", "/certificates/Explore data with MATLAB Plots.pdf"),
        ("Machine Learning Onramp", "/certificates/Machine learning Onramp.pdf"),
        ("Make and Manipulate Matrices", "/certificates/Make and Manipulate Matrices.pdf"),
        ("MATLAB Desktop Tools", "/certificates/MATLAB Desktop tools and Troubleshooting Scripts.pdf"),
        ("MATLAB Onramp", "/certificates/MATLAB Onramp.pdf"),
        ("Simulink Onramp", "/certificates/Simulink Onramp.pdf"),
    ]

    # Hero Profile Layout Banner
    hero = ft.Container(
        bgcolor=CARD,
        border_radius=20,
        padding=30,
        border=ft.Border.all(width=1, color=BORDER_COLOR),
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("WELCOME TO MY PORTFOLIO", size=16, color=SUBTEXT, weight=ft.FontWeight.W_500),
                        ft.Text("ESRA TANGI KALOLA", size=38, weight=ft.FontWeight.BOLD, color=PRIMARY),
                        ft.Text("Mining Engineering Student | Python | MATLAB | Flet", size=18, color=TEXT),
                    ],
                    expand=True,
                ),
                ft.CircleAvatar(foreground_image_src="profile/profile.jpg", radius=70),
            ]
        ),
    )

    # About Me Cards
    about = info_card(
        "About Me",
        "I am a Mining Engineering student passionate about software development, MATLAB, Python programming, engineering problem solving, and mobile application development using Flet.",
    )

    # Tech Stack Framework Container
    skills = ft.Container(
        bgcolor=CARD,
        border_radius=15,
        padding=20,
        border=ft.Border.all(width=1, color=BORDER_COLOR),
        content=ft.Column(
            [
                section_title("Technical Skills"),
                ft.Row(
                    [
                        skill_chip("Python"), skill_chip("MATLAB"), skill_chip("Simulink"),
                        skill_chip("Flet"), skill_chip("Problem Solving"), skill_chip("Engineering"),
                    ],
                    wrap=True,
                ),
            ]
        ),
    )

    # Generate mapped data components
    certificate_controls = [certificate_card(name, file_path) for name, file_path in certificate_data]

    certificates = ft.Container(
        bgcolor=CARD,
        border_radius=15,
        padding=20,
        border=ft.Border.all(width=1, color=BORDER_COLOR),
        content=ft.Column(
            [
                section_title("MATLAB Achievement Hub"),
                ft.Text("Below are my completed MATLAB certificates from MathWorks.", color=SUBTEXT),
                ft.Container(height=10, bgcolor="transparent"),
                ft.Row(certificate_controls, wrap=True, spacing=10),
            ]
        ),
    )

    # Project Development Workflow Milestones Section
    project = ft.Container(
        bgcolor=CARD,
        border_radius=15,
        padding=20,
        border=ft.Border.all(width=1, color=BORDER_COLOR),
        content=ft.Column(
            [
                section_title("Project Timeline"),
                ft.Text("Semester Mobile Application Project: Fix-Flow App", size=20, weight=ft.FontWeight.BOLD, color=TEXT),
                ft.Text("Chronological milestones and technical development steps:", color=SUBTEXT),
                ft.Divider(height=15, color="transparent"),

                timeline_step("Wk 1-2", "Workspace & Initialization", "Configured GitHub repository and coordinated roles."),
                timeline_step("Wk 3-4", "Project Pitching Tracks", "Presented three technical engineering concepts to supervisors."),
                timeline_step("Wk 5-8", "SRS Documentation Phase", "Formulated Software Requirements Specification documentation parameters."),
                timeline_step("Wk 9-12", "UI/UX Graphic Engineering", "Constructed high-fidelity Figma prototypes and user journeys."),
                timeline_step("Wk 5-14", "Application Coding Sprint", "Programmed live application screens and integrated dependencies."),
                timeline_step("Wk 13", "Progress Milestone Proofing", "Executed mid-stage evaluations via a live feature layout demonstration."),
                timeline_step("Wk 14", "Polishing & Build Delivery", "Resolved workflow errors and compiled final documentation."),
                ft.Divider(height=20, color=BORDER_COLOR),

                ft.Text("Project Contribution Documentation Panel:", size=16, weight=ft.FontWeight.BOLD, color=PRIMARY),
                ft.Text("Click below to watch the MP4 video demonstration of our live application workflows natively.", color=SUBTEXT),
                
                ft.Container(height=5, bgcolor="transparent"),
                
                ft.ElevatedButton(
                    content=ft.Row(
                        [ft.Icon(ft.Icons.PLAY_ARROW_ROUNDED), ft.Text("Launch External Media Player")],
                        tight=True,
                    ),
                    on_click=launch_video_file,
                    style=ft.ButtonStyle(
                        color=BG,
                        bgcolor=PRIMARY,
                        shape=ft.RoundedRectangleBorder(radius=8)
                    ),
                ),
            ]
        ),
    )

    contact = ft.Container(
        bgcolor=CARD,
        border_radius=15,
        padding=20,
        border=ft.Border.all(width=1, color=BORDER_COLOR),
        content=ft.Column(
            [
                section_title("Contact"),
                ft.Text("Email: esratangi360@gmail.com", color=TEXT),
                ft.Text("GitHub: github.com/Esra-TK", color=TEXT),
            ]
        ),
    )

    # Assemble Layout Hierarchy onto Canvas
    page.add(
        ft.Column(
            [status_banner, hero, about, skills, certificates, project, contact],
            spacing=20,
        )
    )


# Trigger script run sequence
if __name__ == "__main__":
    ft.run(main, assets_dir="assets")