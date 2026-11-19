"""Verify that new bibliography entries reach every CV without profile edits."""
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


def check(source):
    with tempfile.TemporaryDirectory(prefix="cv-profiles-") as temporary:
        root = Path(temporary)
        cv = root / "CV"
        shutil.copytree(source, cv, ignore=shutil.ignore_patterns("_build", "__pycache__"))
        bib = root / "_bibliography"
        bib.mkdir()
        original = (source.parent / "_bibliography/papers.bib").read_text()
        (bib / "papers.bib").write_text(original + r'''
@article{profilecheckpaper,
  title={ProfilePaperSentinel}, author={Example, Person}, year={2099},
  keywords={published}, url={https://example.com/paper}
}
@software{profilechecksoftware,
  title={ProfileSoftwareSentinel}, note={SharedContentSentinel},
  url={https://example.com/software}
}
''')
        with (root / "build.log").open("w") as log:
            result = subprocess.run(["make", "-j5"], cwd=cv, stdout=log, stderr=subprocess.STDOUT)
        if result.returncode:
            raise RuntimeError((root / "build.log").read_text()[-8000:])
        general_keys = None
        for name in ("cv", "cv-ml", "cv-econ-ai", "cv-genetics", "cv-quant"):
            text = subprocess.check_output(["pdftotext", "-layout", str(cv / "_build" / (name + ".pdf")), "-"], text=True)
            for marker in ("ProfilePaperSentinel", "ProfileSoftwareSentinel", "SharedContentSentinel"):
                assert text.count(marker) == 1, (name, marker)
            bbl = (cv / "_build" / (name + ".bbl")).read_text()
            keys = set(re.findall(r"\\entry\{([^}]+)\}", bbl))
            if general_keys is None:
                general_keys = keys
            assert keys == general_keys, (name, "bibliography entries differ")
            assert text.index("ProfilePaperSentinel") < text.index("Preprints"), name
            assert text.index("Software") < text.index("ProfileSoftwareSentinel"), name
        print("PASS: all five profiles include new papers and software exactly once; bibliography entries and publication groups are preserved.")


if __name__ == "__main__":
    check(Path(__file__).resolve().parent)
