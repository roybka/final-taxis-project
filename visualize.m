cnt=0;
for i=[1:7 9:12]
    cnt=cnt+1;
    filename=['G:\dat\locdat' num2str(i) '.mat']
load(filename)
alltips=alltips{2};

% Nbricks=100;
% rangy=linspace(min(locs(2,:)),max(locs(2,:)),Nbricks);
% rangx=linspace(min(locs(1,:)),max(locs(1,:)),Nbricks);
% [xq,yq] = meshgrid(rangx,rangy);
% vq = griddata(locs(1,:),locs(2,:),alltips,xq,yq);

% figure;mesh(xq,yq,vq);

x1=locs(1,:);
y1=locs(3,:);
x2=locs(2,:);
y2=locs(4,:);
isok=x1~=0 & x2~=0 & y1~=0 & y2~=0;

isok=all(locs~=0,1);
x1=locs(1,isok);
y1=locs(3,isok);
x2=locs(2,isok);
y2=locs(4,isok);
tips=alltips(isok);


a(cnt,:) = [mean(x1(tips==0)) mean(y1(tips==0))]
b(cnt,:) = [ mean(x1(tips>0)) mean(y1(tips>0))]

end
