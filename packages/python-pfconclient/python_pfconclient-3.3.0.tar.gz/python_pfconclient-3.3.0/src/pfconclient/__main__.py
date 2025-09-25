#!/usr/bin/env python3
#
# (c) 2017-2025 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os
from argparse import ArgumentParser

from .client import Client


parser = ArgumentParser(description='Manage pfcon service resources')
parser.add_argument('url', help="url of pfcon service")
parser.add_argument('-a', '--auth_token', help="authorization token for pfcon service")
parser.add_argument('-t', '--timeout', help="requests' timeout")
subparsers = parser.add_subparsers(dest='subparser_name', title='subcommands',
                                   description='valid subcommands',
                                   help='sub-command help')

# create the parser for the "auth" command
parser_auth = subparsers.add_parser('auth', help='get an auth token')
parser_auth.add_argument('--pfcon_user', help="pfcon user", required=True)
parser_auth.add_argument('--pfcon_password', help="pfcon user's password", required=True)

# create the parser for the "run" command
parser_run = subparsers.add_parser('run', help='run a new job until finished')
parser_run.add_argument('inputdir', help="job input directory")
parser_run.add_argument('outputdir', help="job output directory")
run_req_group = parser_run.add_argument_group('required job API parameters')
run_req_group.add_argument('--jid', help="job id", required=True)
run_req_group.add_argument('--args', help='cmd arguments string', required=True)
run_req_group.add_argument('--auid', help='user id', required=True)
run_req_group.add_argument('--number_of_workers', help='number of workers',
                              required=True)
run_req_group.add_argument('--cpu_limit', help='cpu limit', required=True)
run_req_group.add_argument('--memory_limit', help='memory limit', required=True)
run_req_group.add_argument('--gpu_limit', help='gpu limit', required=True)
run_req_group.add_argument('--image', help='docker image', required=True)
run_req_group.add_argument('--selfexec',
                           help='executable file name within the docker image',
                           required=True)
run_req_group.add_argument('--selfpath',
                           help='path to executable file within the docker image',
                           required=True)
run_req_group.add_argument('--execshell',
                           help='execution shell within the docker image',
                           required=True)
run_req_group.add_argument('--type', help='plugin type', choices=['fs', 'ds'],
                           required=True)
run_opt_group = parser_run.add_argument_group('optional job API parameters')
run_opt_group.add_argument('--args_path_flags',
                           help='comma separated list of cmd flags with path argument')
parser_run.add_argument('--poll_initial_wait',
                        help='initial wait time in seconds to poll for job status')
parser_run.add_argument('--poll_max_wait',
                        help='maximum wait time in seconds to poll for job status')

# create the parser for the "submit" command
parser_submit = subparsers.add_parser('submit', help='submit a new job')
parser_submit.add_argument('inputdir', help="job input directory")
submit_req_group = parser_submit.add_argument_group('required job API parameters')
submit_req_group.add_argument('--jid', help="job id", required=True)
submit_req_group.add_argument('--args', help='cmd arguments string', required=True)
submit_req_group.add_argument('--auid', help='user id', required=True)
submit_req_group.add_argument('--number_of_workers', help='number of workers', required=True)
submit_req_group.add_argument('--cpu_limit', help='cpu limit', required=True)
submit_req_group.add_argument('--memory_limit', help='memory limit', required=True)
submit_req_group.add_argument('--gpu_limit', help='gpu limit', required=True)
submit_req_group.add_argument('--image', help='docker image', required=True)
submit_req_group.add_argument('--selfexec',
                              help='executable file name within the docker image',
                              required=True)
submit_req_group.add_argument('--selfpath',
                              help='path to executable file within the docker image',
                              required=True)
submit_req_group.add_argument('--execshell',
                              help='execution shell within the docker image',
                              required=True)
submit_req_group.add_argument('--type', help='plugin type', choices=['fs', 'ds'],
                              required=True)
submit_opt_group = parser_submit.add_argument_group('optional job API parameters')
submit_opt_group.add_argument('--args_path_flags',
                              help='comma separated list of cmd flags with path argument')

# create the parser for the "status" command
parser_status = subparsers.add_parser('status', help='get the exec status of a job')
parser_status.add_argument('--jid', help="job id", required=True)

# create the parser for the "poll" command
parser_poll = subparsers.add_parser('poll',
                                    help='poll the exec status of a job until finished')
parser_poll.add_argument('--jid', help="job id", required=True)
parser_poll.add_argument('--poll_initial_wait',
                         help='initial wait time in seconds to poll for job status')
parser_poll.add_argument('--poll_max_wait',
                         help='maximum wait time in seconds to poll for job status')

# create the parser for the "download" command
parser_download = subparsers.add_parser('download',
                                        help="download job's output files")
parser_download.add_argument('--jid', help="job id", required=True)
parser_download.add_argument('outputdir', help="directory to download job's output files")
parser_download.add_argument('--zip', action='store_true',
                             help='save output files as a single zip file')

# create the parser for the "delete" command
parser_delete = subparsers.add_parser('delete', help='delete an existing job')
parser_delete.add_argument('--jid', help="job id", required=True)


def main():
    # parse the arguments and perform the appropriate action with the client
    args = parser.parse_args()
    timeout = args.timeout or 1000

    if args.subparser_name == 'auth':
        auth_url = args.url + 'auth-token/'
        token = Client.get_auth_token(auth_url, args.pfcon_user, args.pfcon_password)
        print(f'\ntoken: {token}\n')
    else:
        cl = Client(args.url, args.auth_token)

        if args.subparser_name == 'run' or args.subparser_name == 'submit':
            d_job_descriptors = {
                'entrypoint': [args.execshell, os.path.join(args.selfpath, args.selfexec)],
                'args': args.args.split(),
                'args_path_flags': args.args_path_flags if args.args_path_flags is not None else '',
                'auid': args.auid,
                'number_of_workers': args.number_of_workers,
                'cpu_limit': args.cpu_limit,
                'memory_limit': args.memory_limit,
                'gpu_limit': args.gpu_limit,
                'image': args.image,
                'type': args.type
            }

            if args.subparser_name == 'run':
                if args.poll_initial_wait:
                    cl.initial_wait = args.poll_initial_wait

                if args.poll_max_wait:
                    cl.max_wait = args.poll_max_wait
                cl.run_job(args.jid, d_job_descriptors, args.inputdir, args.outputdir,
                               timeout)
            else:
                # create job zip file content from local input_dir
                job_zip_file = cl.create_zip_file(args.inputdir)
                zip_content = job_zip_file.getvalue()
                cl.submit_job(args.jid, d_job_descriptors, zip_content, timeout)

        elif args.subparser_name == 'status':
            d_resp = cl.get_job_status(args.jid, timeout)
            status = d_resp['compute']['status']
            print('\nJob %s status: %s' % (args.jid, status))

        elif args.subparser_name == 'poll':
            if args.poll_initial_wait:
                cl.initial_wait = args.poll_initial_wait

            if args.poll_max_wait:
                cl.max_wait = args.poll_max_wait
            cl.poll_job_status(args.jid, timeout)

        elif args.subparser_name == 'download':
            if args.zip:
                cl.get_job_zip_file(args.jid, args.outputdir, timeout)
            else:
                cl.get_job_files(args.jid, args.outputdir, timeout)

        elif args.subparser_name == 'delete':
            cl.delete_job(args.jid, timeout)
            print('\nDeleted job %s' % args.jid)


if __name__ == "__main__":
    main()
