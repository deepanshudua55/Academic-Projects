// Project Hadoop
	
	import java.io.IOException;
	import java.util.*;
	
	import org.apache.hadoop.fs.Path;
	import org.apache.hadoop.conf.*;
	import org.apache.hadoop.io.*;
	import org.apache.hadoop.mapred.*;
	import org.apache.hadoop.util.*;
	
	public class Sarvesh {
	
	    public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, IntWritable, DoubleWritable> {
	      //private final static IntWritable one = new IntWritable(1);
	      //private Text word = new Text();
	
	      public void map(LongWritable key, Text value, OutputCollector<IntWritable, DoubleWritable> output, Reporter reporter) throws IOException {
	        String line = value.toString();
	        StringTokenizer stringTokenizer = new StringTokenizer(line, "|");
	        while (stringTokenizer.hasMoreElements()) {
	        	stringTokenizer.nextElement();
	        	Integer cust = Integer.parseInt(stringTokenizer.nextElement().toString());
	        	stringTokenizer.nextElement().toString();
	        	Double p = Double.parseDouble(stringTokenizer.nextElement().toString());
	        	stringTokenizer.nextElement();
	        	stringTokenizer.nextElement();
	        	stringTokenizer.nextElement();
	        	stringTokenizer.nextElement();
	        	stringTokenizer.nextElement();
	        	//System.out.println("Custkey: "+cust+" Price: "+p);
	            output.collect(new IntWritable(cust), new DoubleWritable(p));
	          //continue;
	        }
	      }
	    }
	
	    public static class Reduce extends MapReduceBase implements Reducer<IntWritable, DoubleWritable, IntWritable, DoubleWritable> {
	      public void reduce(IntWritable key, Iterator<DoubleWritable> values, OutputCollector<IntWritable, DoubleWritable> output, Reporter reporter) throws IOException {
	        int sum = 0;
	        while (values.hasNext()) {
	          sum += values.next().get();
	        }
	        output.collect(key, new DoubleWritable(sum));
	      }
	    }
	
	    public static void main(String[] args) throws Exception {
	      JobConf conf = new JobConf(Sarvesh.class);
	      conf.setJobName("sarvesh");
	
	      conf.setOutputKeyClass(IntWritable.class);
	      conf.setOutputValueClass(DoubleWritable.class);
	
	      conf.setMapperClass(Map.class);
	      conf.setCombinerClass(Reduce.class);
	      conf.setReducerClass(Reduce.class);
	
	      conf.setInputFormat(TextInputFormat.class);
	      conf.setOutputFormat(TextOutputFormat.class);
	
	      FileInputFormat.setInputPaths(conf, new Path(args[0]));
	      FileOutputFormat.setOutputPath(conf, new Path(args[1]));
	
	      JobClient.runJob(conf);
	    }
	}