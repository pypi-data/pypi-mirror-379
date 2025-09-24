import os
import tkinter as tk
from tkinter import Canvas
from . import theme


class Controls:
    def __init__(self, parent, videoplayer):
        # Store reference to videoplayer
        self.videoplayer = videoplayer
        self._slider_dragging = False  # Track if slider is being dragged

        # Subscribe to video player events
        videoplayer.add_event_listener("play", self._on_play)
        videoplayer.add_event_listener("pause", self._on_pause)
        videoplayer.add_event_listener("ended", self._on_ended)

        self.frame = tk.Frame(parent, bg=theme.COLOR_CONTROLS_BG)
        self.frame.pack(fill=tk.X, padx=10, pady=5)

        # Play/Pause Button (icon)
        self.is_playing = False

        # Load icons for play and pause
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.play_icon = tk.PhotoImage(file=os.path.join(base_dir, "media", "play.png"))
        self.pause_icon = tk.PhotoImage(file=os.path.join(base_dir, "media", "pause.png"))

        self.play_pause_btn = tk.Button(
            self.frame,
            image=self.play_icon,
            bg=theme.COLOR_CONTROLS_BG,
            activebackground=theme.COLOR_CONTROLS_BG,
            bd=0,
            command=self._toggle_play_pause,
        )
        self.play_pause_btn.pack(side=tk.LEFT, padx=(16, 8))

        # Time Counter
        self.time_label = tk.Label(
            self.frame, text="0:00 / 0:00", font=theme.FONT, bg=theme.COLOR_CONTROLS_BG, fg=theme.COLOR_SLIDER_BG
        )
        self.time_label.pack(side=tk.LEFT, padx=8)

        # Custom Thin Slider
        self.slider_height = 8  # Visual height of the slider line
        self.slider_clickable_height = 28  # Height of the clickable area (matches font size)
        self.slider_canvas = Canvas(
            self.frame,
            height=self.slider_clickable_height,
            bg=theme.COLOR_CONTROLS_BG,
            highlightthickness=0,
        )
        self.slider_canvas.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)
        self.slider_canvas.bind("<Button-1>", self._on_slider_click)
        self.slider_canvas.bind("<B1-Motion>", self._on_slider_drag)
        self.slider_canvas.bind("<ButtonRelease-1>", self._on_slider_release)
        self.slider_canvas.bind("<Configure>", self._on_slider_resize)
        self.slider_value = 0
        self.slider_max = 100

        self._draw_slider()

        # Start update timer for displaying current time
        self._start_timer()

    def _on_slider_resize(self, event):
        """Redraw slider when the canvas is resized."""
        self._draw_slider()

    def _on_play(self):
        self.is_playing = True
        self._update_play_pause_button()

    def _on_pause(self):
        self.is_playing = False
        self._update_play_pause_button()

    def _on_ended(self):
        self.is_playing = False
        self._update_play_pause_button()

    def _start_timer(self):
        """Start a timer to update the time display and slider position"""
        # Check if the frame still exists before scheduling the next update
        if not self.frame.winfo_exists():
            return  # Frame was destroyed, don't schedule any more updates

        self._update_display()
        self.frame.after(250, self._start_timer)

    def _update_display(self):
        """Update time display and slider position based on current video state"""
        try:
            # First check if our widgets still exist before updating
            if not self.frame.winfo_exists():
                return

            # Ensure button state matches videoplayer state
            # This ensures UI stays in sync even if events are missed
            if hasattr(self, "videoplayer"):
                playing_state = self.videoplayer.playing and not self.videoplayer.paused
                if self.is_playing != playing_state:
                    self.is_playing = playing_state
                    self._update_play_pause_button()

            current_time = self.videoplayer.currentTime
            total_time = self.videoplayer.duration

            # Update time display
            self.update_time(current_time, total_time)

            # Update slider position only if not dragging
            if not self._slider_dragging and total_time > 0:
                self.set_slider(current_time, total_time)
        except Exception as e:
            # Print errors to debug
            print(f"Error updating display: {e}")
            # Silently continue
            pass

    def _toggle_play_pause(self):
        if self.is_playing:
            self.videoplayer.pause()
        else:
            self.videoplayer.play()

    def _update_play_pause_button(self):
        """Update the play/pause button icon based on current state"""
        # Check if the button still exists before trying to update it
        if not hasattr(self, "play_pause_btn") or not self.play_pause_btn.winfo_exists():
            return

        if self.is_playing:
            self.play_pause_btn.config(image=self.pause_icon)
        else:
            self.play_pause_btn.config(image=self.play_icon)

    def update_time(self, current, total):
        # Check if label still exists before updating
        if hasattr(self, "time_label") and self.time_label.winfo_exists():
            self.time_label.config(text=f"{self._format_time(current)} / {self._format_time(total)}")

    def _format_time(self, seconds):
        m, s = divmod(int(seconds), 60)
        return f"{m}:{s:02d}"

    def set_slider(self, value, max_value):
        self.slider_value = value
        self.slider_max = max_value
        self._draw_slider()

    def _draw_slider(self):
        # Check if slider canvas still exists
        if not hasattr(self, "slider_canvas") or not self.slider_canvas.winfo_exists():
            return

        self.slider_canvas.delete("all")
        # Internal horizontal padding to prevent knob cutoff
        slider_padding = 8
        slider_length = self.slider_canvas.winfo_width()
        usable_length = max(0, slider_length - 2 * slider_padding)
        center_y = self.slider_clickable_height // 2
        # Draw background line (thin)
        self.slider_canvas.create_line(
            slider_padding,
            center_y,
            slider_length - slider_padding,
            center_y,
            fill=theme.COLOR_TERTIARY,
            width=3,
        )
        # Draw progress line
        if self.slider_max > 0:
            progress = int((self.slider_value / self.slider_max) * usable_length) + slider_padding
        else:
            progress = slider_padding
        self.slider_canvas.create_line(
            slider_padding,
            center_y,
            progress,
            center_y,
            fill=theme.COLOR_PRIMARY,
            width=3,
        )
        # Draw draggable knob (thin, centered)
        self.slider_canvas.create_oval(
            progress - 5,
            center_y - 5,
            progress + 5,
            center_y + 5,
            fill=theme.COLOR_PRIMARY,
            outline=theme.COLOR_PRIMARY,
        )

    def _on_slider_click(self, event):
        self._seek_to(event.x, immediate=True)

    def _on_slider_drag(self, event):
        self._slider_dragging = True
        # Update slider visually, but don't seek immediately during drag
        self._seek_to(event.x, immediate=False)

    def _on_slider_release(self, event):
        # Perform the actual seek when the slider is released
        self._seek_to(event.x, immediate=True)
        self._slider_dragging = False

    def _seek_to(self, x, immediate=True):
        # Use current slider width for calculation
        slider_length = self.slider_canvas.winfo_width()
        value = (x / slider_length) * self.slider_max
        value = max(0, min(self.slider_max, value))
        self.set_slider(value, self.slider_max)

        if immediate:
            self.videoplayer.currentTime = value
