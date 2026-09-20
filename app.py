"""Thin entry stub: load profile → hand off to a private CloudDoor plugin."""

from __future__ import annotations

import streamlit as st

from gtbs_kit.load_profile import load_profile


def main() -> None:
    st.title("GBTS Chip Service Kit")
    st.caption("Load a profile, then call your private CloudDoor implementation.")
    path = st.text_input("Profile YAML", "profiles/examples/grapevine_167k/profile.yaml")
    if st.button("Validate profile") and path:
        st.json(load_profile(path))


if __name__ == "__main__":
    main()
