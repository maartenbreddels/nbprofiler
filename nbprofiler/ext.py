from notebook.base.handlers import IPythonHandler
from notebook.utils import url_path_join
import os
basedir = os.path.dirname(__file__)
import cProfile
import tornado
import notebook
import contextlib
try:
	from io import BytesIO as StringIO # python3
except:
	from StringIO import StringIO # python2

# from http://stackoverflow.com/questions/8495422/use-a-context-manager-for-python-script-output-to-a-file
@contextlib.contextmanager
def redirect_stdout(stream):
    import sys
    sys.stdout = stream
    yield
    sys.stdout = sys.__stdout__


class ProfileHandler(IPythonHandler):
	profiler = None
	start_times = None
	end_times = None

	def get_profiler(self):
		if ProfileHandler.profiler is None:
			ProfileHandler.profiler = cProfile.Profile()
		return ProfileHandler.profiler

	def get(self):
		#self.finish('Hello, world!')
		print(self.request.path)
		parts = self.request.path.split('/')
		print(parts)
		profiler = self.get_profiler()
		action = parts[2]
		if action == "start":
			profiler.enable()
			ProfileHandler.start_times = os.times()
			self.finish("enable ok")
		elif action == "stop":
			profiler.disable()
			ProfileHandler.end_times = os.times()
			self.finish("disable ok")
		elif action == "clear":
			profiler.clear()
			self.finish("clear ok")
		elif action == "report":
			import pstats
			sort = -1
			if len(parts) > 3:
				sort = parts[3]
			pstats.Stats(profiler, stream=self).strip_dirs().sort_stats(sort).print_stats()
			utime0, stime0, child_utime0, child_stime0, walltime0 = ProfileHandler.start_times
			end_times = ProfileHandler.end_times or os.times()
			utime, stime, child_utime, child_stime, walltime = end_times
			with redirect_stdout(self):
				print("user time:            % 9.3f sec." % (utime - utime0))
				print("system time:          % 9.3f sec." % (stime - stime0))
				print("user time(children):  % 9.3f sec." % (child_utime - child_utime0))
				print("system time(children):% 9.3f sec." % (child_stime - child_stime0))
				print("elapsed time:         % 9.3f sec. (normal wallclock time it took)" % (walltime - walltime0))
			self.finish("print ok")
		else:
			self.finish("unknown request: %r " % (parts,))


def load_jupyter_server_extension(nb_server_app):
	print(nb_server_app)
	web_app = nb_server_app.web_app
	host_pattern = '.*$'
	route_pattern = url_path_join(web_app.settings['base_url'], '/profiler')
	print(route_pattern)
	web_app.add_handlers(host_pattern, [
		(url_path_join(web_app.settings['base_url'], '/profiler/.*'), ProfileHandler)
	])