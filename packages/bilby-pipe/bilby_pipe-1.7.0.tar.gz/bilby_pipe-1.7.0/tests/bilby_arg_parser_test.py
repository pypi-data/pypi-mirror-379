import os
import shutil
import sys
import unittest
from unittest.mock import patch

import bilby
from bilby_pipe.bilbyargparser import BilbyArgParser
from bilby_pipe.data_analysis import create_analysis_parser
from bilby_pipe.main import parse_args
from bilby_pipe.parser import create_parser
from bilby_pipe.utils import convert_prior_string_input, convert_string_to_dict


class TestBilbyArgParser(unittest.TestCase):
    def setUp(self):
        self.directory = os.path.abspath(os.path.dirname(__file__))
        self.outdir = "outdir"

    def tearDown(self):
        if os.path.exists(self.outdir):
            shutil.rmtree(self.outdir)

    def test_normalising_args(self):
        args_list = ["--sample_kwargs={'a':1}", "--_n=param"]
        bbargparser = BilbyArgParser()
        args, unknown_args = bbargparser.parse_known_args(args_list)
        self.assertTrue("param" in unknown_args)
        self.assertTrue("--sample-kwargs" in unknown_args)

    def test_args_string(self):
        bbargparser = BilbyArgParser()
        arg_key = "--key"
        arg_val = "val"
        args_string = f"{arg_key} {arg_val}"
        args, unknown_args = bbargparser.parse_known_args(args=args_string)
        self.assertTrue(arg_val in unknown_args)

    def test_arg_input_from_sys(self):
        bbargparser = BilbyArgParser()
        arg_key = "--key"
        arg_val = "val"
        args_list = [arg_key, arg_val]
        with patch.object(sys, "argv", args_list):
            args, unknown_args = bbargparser.parse_known_args()
            self.assertTrue(arg_val in unknown_args)

    def test_detectors_single(self):
        args_list = [
            "tests/test_dag_ini_file.ini",
            "--detectors",
            "H1",
            "--detectors",
            "L1",
        ]
        parser = create_analysis_parser()
        args, unknown_args = parse_args(args_list, parser)
        self.assertNotEqual(args.detectors, ["'H1'", "'L1'"], args.detectors)
        self.assertEqual(args.detectors, ["H1", "L1"], args.detectors)

    def test_detectors_double(self):
        args_list = ["tests/test_bilbyargparser.ini"]
        parser = create_analysis_parser()
        args, unknown_args = parse_args(args_list, parser)
        self.assertNotEqual(args.detectors, ["'H1'", "'L1'"], args.detectors)
        self.assertEqual(args.detectors, ["H1", "L1"], args.detectors)


class TestBilbyConfigFileParser(unittest.TestCase):
    def setUp(self):
        self.test_ini_filename = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "TEST_CONFIG.ini"
        )
        self.parser = create_parser(top_level=True)

    def tearDown(self):
        if os.path.exists(self.test_ini_filename):
            os.remove(self.test_ini_filename)

    def write_tempory_ini_file(self, lines):
        lines.append("accounting: test")
        with open(self.test_ini_filename, "a") as file:
            for line in lines:
                print(line, file=file)

        print(f"File{self.test_ini_filename}, content:")
        print("-------BEGIN-------")
        with open(self.test_ini_filename, "r") as file:
            for line in file:
                print(line.replace("\n", ""))
        print("-------END---------")

    def test_simple(self):
        self.write_tempory_ini_file([])
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        self.assertEqual(args.accounting, "test")

    def test_accounting_user(self):
        lines = ["accounting_user: albert.einstein"]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        self.assertEqual(args.accounting_user, "albert.einstein")

    def test_sampler_kwargs_flat(self):
        kwargs_expected = dict(walks=1000)
        lines = ["sampler-kwargs: {walks:1000}"]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        self.assertEqual(convert_string_to_dict(args.sampler_kwargs), kwargs_expected)

    def test_sampler_kwargs_flat_multiline(self):
        kwargs_expected = dict(walks=1000, nact=5)
        lines = ["sampler-kwargs: {walks:1000,", "nact=5}"]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        self.assertEqual(convert_string_to_dict(args.sampler_kwargs), kwargs_expected)

    def test_sampler_kwargs_flat_multiline_no_comma(self):
        kwargs_expected = dict(walks=1000, nact=5)
        lines = ["sampler-kwargs: {walks:1000", "nact=5}"]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        self.assertEqual(convert_string_to_dict(args.sampler_kwargs), kwargs_expected)

    def test_sampler_kwargs_flat_multiline_with_space(self):
        kwargs_expected = dict(walks=1000, nact=5)
        lines = ["sampler-kwargs: {walks:1000", "   nact=5}"]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        self.assertEqual(convert_string_to_dict(args.sampler_kwargs), kwargs_expected)

    def test_sampler_kwargs_flat_multiline_end_comma(self):
        kwargs_expected = dict(walks=1000, nact=5)
        lines = ["sampler-kwargs: {walks:1000", "   nact=5,}"]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        self.assertEqual(convert_string_to_dict(args.sampler_kwargs), kwargs_expected)

    def test_sampler_kwargs_flat_long_multiline(self):
        kwargs_expected = dict(walks=1000, nact=5, test=1, blah="a")
        lines = ["sampler-kwargs: {walks:1000", "nact=5, test:1", "    blah=a}"]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        self.assertEqual(convert_string_to_dict(args.sampler_kwargs), kwargs_expected)

    def test_sampler_kwargs_empty(self):
        kwargs_expected = dict()
        kwargs_str = "{}"
        lines = [f"sampler-kwargs: {kwargs_str}"]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        self.assertEqual(convert_string_to_dict(args.sampler_kwargs), kwargs_expected)

    def test_prior_dict(self):
        kwargs_str = '{a=Uniform(name="a", minimum=0, maximum=1)}'
        lines = [f"prior-dict: {kwargs_str}"]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        self.assertEqual(args.prior_dict, kwargs_str)
        self.assertEqual(unknown_args, [])

    def test_prior_dict_multiline(self):
        kwargs_str = "{a: Uniform(name='a', minimum=0, maximum=1), b: 1}"
        lines = ["prior-dict: {a: Uniform(name='a', minimum=0, maximum=1)", "b: 1}"]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        self.assertEqual(args.prior_dict, kwargs_str)
        self.assertEqual(unknown_args, [])

    def test_prior_dict_multiline_complicated1(self):
        expected_prior = bilby.core.prior.PriorDict(
            dict(
                a=bilby.core.prior.Uniform(name="a", minimum=0, maximum=1),
                b=1,
                c=2,
                redshift=bilby.gw.prior.UniformSourceFrame(
                    name="redshift",
                    minimum=1,
                    maximum=10,
                    latex_label=r"$\rm{log}_{10}(M_{Lz}/\rm M_\odot)$",
                ),
            )
        )
        lines = [
            "prior-dict: {a: Uniform(name='a', minimum=0, maximum=1),",
            "b: 1,",
            "  c: 2,",
            r"redshift: bilby.gw.prior.UniformSourceFrame(name='redshift',"
            + r"minimum=1, maximum=10, latex_label='$\rm{log}_{10}(M_{Lz}/\rm M_\odot)$')",
            "}",
        ]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        prior = bilby.core.prior.PriorDict(convert_prior_string_input(args.prior_dict))
        self.assertEqual(expected_prior, prior)
        self.assertEqual(unknown_args, [])

    def test_prior_dict_multiline_complicated2(self):
        expected_prior = bilby.core.prior.PriorDict(
            dict(
                a=bilby.core.prior.Uniform(name="a", minimum=0, maximum=1),
                b=1,
                c=2,
                redshift=bilby.gw.prior.UniformSourceFrame(
                    name="redshift",
                    minimum=1,
                    maximum=10,
                    latex_label=r"$\rm{log}_{10}(M_{Lz}/\rm M_\odot)$",
                ),
            )
        )
        lines = [
            "prior-dict: {a: Uniform(name='a', minimum=0, maximum=1),",
            "b: 1,",
            "  c: 2,",
            r"redshift: bilby.gw.prior.UniformSourceFrame(name='redshift',"
            + r"minimum=1, maximum=10, latex_label='$\rm{log}_{10}(M_{Lz}/\rm M_\odot)$'),",
            "}",
        ]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        prior = bilby.core.prior.PriorDict(convert_prior_string_input(args.prior_dict))
        self.assertEqual(expected_prior, prior)
        self.assertEqual(unknown_args, [])

    def test_prior_dict_multiline_complicated3(self):
        expected_prior = bilby.core.prior.PriorDict(
            dict(
                a=bilby.core.prior.Uniform(name="a", minimum=0, maximum=1),
                b=1,
                c=2,
                redshift=bilby.gw.prior.UniformSourceFrame(
                    name="redshift",
                    minimum=1,
                    maximum=10,
                    latex_label=r"$\rm{log}_{10}(M_{Lz}/\rm M_\odot)$",
                ),
            )
        )
        lines = [
            "prior-dict: {a: Uniform(name='a', minimum=0, maximum=1),",
            "b: 1,",
            "  c: 2,",
            r"redshift: bilby.gw.prior.UniformSourceFrame(name='redshift',"
            + r"minimum=1, maximum=10, latex_label='$\rm{log}_{10}(M_{Lz}/\rm M_\odot)$')}",
        ]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        prior = bilby.core.prior.PriorDict(convert_prior_string_input(args.prior_dict))
        self.assertEqual(expected_prior, prior)
        self.assertEqual(unknown_args, [])

    def test_prior_dict_multiline_complicated4(self):
        expected_prior = bilby.core.prior.PriorDict(
            dict(
                a=bilby.core.prior.Uniform(name="a", minimum=0, maximum=1),
                b=1,
                c=2,
                redshift=bilby.gw.prior.UniformSourceFrame(
                    name="redshift",
                    minimum=1,
                    maximum=10,
                    latex_label=r"$\rm{log}_{10}(M_{Lz}/\rm M_\odot)$",
                ),
            )
        )
        lines = [
            "prior-dict: {a: Uniform(name='a', minimum=0, maximum=1),",
            "b: 1,",
            r"redshift: bilby.gw.prior.UniformSourceFrame(name='redshift',"
            + r"minimum=1, maximum=10, latex_label='$\rm{log}_{10}(M_{Lz}/\rm M_\odot)$'),"
            "  c: 2}",
        ]
        self.write_tempory_ini_file(lines)
        args, unknown_args = parse_args([self.test_ini_filename], self.parser)
        prior = bilby.core.prior.PriorDict(convert_prior_string_input(args.prior_dict))
        self.assertEqual(expected_prior, prior)
        self.assertEqual(unknown_args, [])

    def test_scitoken_issuer_fails_for_unknown_value(self):
        self.write_tempory_ini_file([])
        args_list = [self.test_ini_filename, "--scitoken-issuer", "test"]
        with self.assertRaises(SystemExit):
            parse_args(args_list, self.parser)

    def test_scitoken_issuer_allowed_values(self):
        self.write_tempory_ini_file([])
        values = ["None", "igwn", "local"]
        expected = [None, "igwn", "local"]
        for value, exp in zip(values, expected):
            args_list = [self.test_ini_filename, "--scitoken-issuer", value]
            args = parse_args(args_list, self.parser)[0]
            assert args.scitoken_issuer == exp


if __name__ == "__main__":
    unittest.main()
