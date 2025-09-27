// MIT License
//
// Copyright (c) 2023 Astral Software Inc.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

use anstream::{eprint, print};
use indicatif::ProgressDrawTarget;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Printer {
    /// A printer that prints to standard streams (e.g., stdout).
    Default,
    /// A printer that suppresses all output.
    Quiet,
    /// A printer that prints all output, including debug messages.
    Verbose,
    /// A printer that prints to standard streams, excluding all progress outputs
    NoProgress,
}

impl Printer {
    /// Return the [`ProgressDrawTarget`] for this printer.
    pub fn target(self) -> ProgressDrawTarget {
        match self {
            Self::Default => ProgressDrawTarget::stderr(),
            Self::Quiet => ProgressDrawTarget::hidden(),
            // Confusingly, hide the progress bar when in verbose mode.
            // Otherwise, it gets interleaved with debug messages.
            Self::Verbose => ProgressDrawTarget::hidden(),
            Self::NoProgress => ProgressDrawTarget::hidden(),
        }
    }

    /// Return the [`Stdout`] for this printer.
    pub fn stdout(self) -> Stdout {
        match self {
            Self::Default => Stdout::Enabled,
            Self::Quiet => Stdout::Disabled,
            Self::Verbose => Stdout::Enabled,
            Self::NoProgress => Stdout::Enabled,
        }
    }

    /// Return the [`Stderr`] for this printer.
    pub fn stderr(self) -> Stderr {
        match self {
            Self::Default => Stderr::Enabled,
            Self::Quiet => Stderr::Disabled,
            Self::Verbose => Stderr::Enabled,
            Self::NoProgress => Stderr::Enabled,
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Stdout {
    Enabled,
    Disabled,
}

impl std::fmt::Write for Stdout {
    fn write_str(&mut self, s: &str) -> std::fmt::Result {
        match self {
            Self::Enabled => {
                #[allow(clippy::print_stdout, clippy::ignored_unit_patterns)]
                {
                    print!("{s}");
                }
            }
            Self::Disabled => {}
        }

        Ok(())
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Stderr {
    Enabled,
    Disabled,
}

impl std::fmt::Write for Stderr {
    fn write_str(&mut self, s: &str) -> std::fmt::Result {
        match self {
            Self::Enabled => {
                #[allow(clippy::print_stderr, clippy::ignored_unit_patterns)]
                {
                    eprint!("{s}");
                }
            }
            Self::Disabled => {}
        }

        Ok(())
    }
}
